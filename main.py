import sqlite3
import os
import time
from sage.all import *


def create_tables(c, A: int, RANGE: int) -> None:
    """
    """

    for a in range(A, A+RANGE):
        if a < 0:
            a = f"neg_{-a}"
        try:
            c.execute(f"""CREATE TABLE _{a} (
                    p integer,
                    multi_order integer, 
                    prim_root integer,
                    Omega_Omega integer,
                    o_o integer,
                    o_ integer
                    )"""
                    )
        except sqlite3.OperationalError as e:
            print(e)

    # print("SQL Warning: tables", error_a, "already exist")


def insert_entry(c,
                 a, 
                 p, 
                 order, 
                 prim_root, 
                 Omega_Omega, 
                 o_o, 
                 o_) -> None:
    """
    """
    if a < 0:
        table_name = f"_neg_{-a}"
    else:
        table_name = f"_{a}"

    c.execute(f"INSERT INTO {table_name} VALUES (:p, :multi_order, :prim_root, :Omega_Omega, :o_o, :o_)",
              {"p": p, "multi_order": order, "prim_root": prim_root, "Omega_Omega": Omega_Omega, "o_o": o_o, "o_": o_ })



def factorize(integer: int) -> tuple[int, int]:
    """
    """
    # no multiplicity
    F = factor(integer)
    omega = len(F)

    # multiplicity
    Omega = 0
    for factor_val, multiplicity in list(F):
        Omega += multiplicity
    
    return(int(omega), int(Omega))


def order_a_mod_p(a: int, p: int) -> int:
    """
    """
    if Mod(a,p):
        order = Mod(a,p).multiplicative_order()
    else:
        order = 0
    return int(order)


if __name__ == "__main__":
    A = -400
    P = 0
    RANGE = 800
    PRIMES = 10000

    start_time_total = time.time()

    # connect 
    conn = sqlite3.connect("artin.db")
    c = conn.cursor()
    primes = Primes()
    # create tables
    create_tables(c, A, RANGE)
    conn.commit()

    # compute values 
    for a in range(A, A+RANGE):
        start_time = time.time()

        for prime_index in range(P, P+PRIMES):
            prime = int(primes.unrank(prime_index))

            if a < 0:
                c.execute(f"SELECT * FROM _neg_{-a} WHERE p = :p",
                      {"p": prime})
            else:
                c.execute(f"SELECT * FROM _{a} WHERE p = :p",
                        {"p": prime})
            
            if c.fetchone() is None:
                order = order_a_mod_p(a, prime)

                prim_root_mod_p = 0
                if order == (prime - 1):
                    prim_root_mod_p = 1
                
                if order != 0:
                    # calculate the exponents 
                    omega_orda, Omega_orda = factorize(order)
                    omega_p_1, Omega_p_1 = factorize(prime-1)
                    o_, O_ = factorize(int((prime-1)/order))
                    Omega_Omega = Omega_p_1 - Omega_orda
                    o_o = omega_p_1 - omega_orda

                    insert_entry(c, a, prime, order, prim_root_mod_p, Omega_Omega, o_o, o_)
                else:
                    insert_entry(c, a, prime, order, 0, -1, -1, -1)

        print(f"a = {a}", time.time() - start_time, "s")
        # commit 
        conn.commit()

    # disconnect
    conn.close()
    print(f"Total", time.time() - start_time_total, "s")