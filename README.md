# Artin-s-Conjecture-Data-Collection

## GETTING STARTED

1. SageMath - install sagemath (https://doc.sagemath.org/html/en/installation/index.html) or use a cloud service (such
   as CoCal) that can run Sage files
2. Customizing Parameters - There are 4 parameters to specify. A, P, RANGE, PRIMES in main.py
   - A: int = starting A value.
   - P: int+ or 0 = starting prime index. EX: P = 0 would make the first prime 2.
   - RANGE: int+ = number of As to iterate through from A. EX: A = 0, RANGE = 10 would go through a in {0, 1, 2, ..., 9}.
   - PRIMES: int+ = number of primes to iterate through from P. EX: P = 0, PRIMES = 2 would go through {2, 3}.
     Note that to save time, the program does not check whether data already exists or not. And any new computation is
     inserted directly to the end of the database (not sorted).
3. In a terminal, run "sage main.py"
4. The result will be in a database base in the same directory called "artin.db"

## Some Time References

1. 10000 primes takes a little less than 0.5 seconds for each a
2. 100000 primes takes a little less than 20 seconds for each a
