# Artin-s-Conjecture-Data-Collection

## GETTING STARTED

1. SageMath - install sagemath (https://doc.sagemath.org/html/en/installation/index.html) or use a cloud service (such
   as CoCal) that can run .sage files. Run this command to ensure SageMath is installed correctly (make sure to install
   any optional packages they offer to ensure the command line interface is setup).
<img width="500" alt="Screen Shot 2023-09-01 at 8 17 04 PM" src="https://github.com/YouTelllMe/Artin-s-Conjecture-Data-Collection/assets/80024712/17895426-2b2a-45bd-897c-bcaa32f48557">

3. Customizing Parameters - There are 4 parameters to specify. A, P, RANGE, PRIMES in main.py
   - A: int = starting A value.
   - P: int+ or 0 = starting prime index. EX: P = 0 would make the first prime 2.
   - RANGE: int+ = number of As to iterate through from A. EX: A = 0, RANGE = 10 would go through a in {0, 1, 2, ..., 9}.
   - PRIMES: int+ = number of primes to iterate through from P. EX: P = 0, PRIMES = 5 would go through {2, 3, 5, 7, 11}.
     Note that to save time, the program does not check whether data already exists or not. And any new computation is
     inserted directly to the end of the database (not sorted).
<img width="600" alt="Screen Shot 2023-09-01 at 8 13 21 PM" src="https://github.com/YouTelllMe/Artin-s-Conjecture-Data-Collection/assets/80024712/a6406c76-aa6e-4716-9a91-02e91e09c6bf">

4. In a terminal, run "sage main.py"
5. The result will be a .db in the same directory called "artin.db" with columns
<img width="600" alt="Screen Shot 2023-09-01 at 8 14 55 PM" src="https://github.com/YouTelllMe/Artin-s-Conjecture-Data-Collection/assets/80024712/1735b847-14d0-4608-b16a-34eab7c03491">

TABLE NAME: corresponds to an A value<br />
p: prime <br />
multi_order: order a mod p<br />
prim_root: boolean field for whether a is a primitive root mod p<br />
Omega-Omega: Ω - Ω<br />
o_o: ω - ω<br />
o_: ω(/)<br />

## Some Time References

1. 1000 primes takes a little less than 0.05 for each a
1. 10000 primes takes a little less than 0.5 seconds for each a
1. 100000 primes takes a little less than 20 seconds for each a
