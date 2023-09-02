# Artin-s-Conjecture-Data-Collection

## GETTING STARTED

1. SageMath - install sagemath (https://doc.sagemath.org/html/en/installation/index.html) or use a cloud service (such
   as CoCal) that can run Sage files
2. Customizing Parameters - There are 4 parameters to specify. A, P, RANGE, PRIMES in main.py
   - A: int = starting A value.
   - P: int+ or 0 = starting prime index. EX: P = 0 would make the first prime 2.
   - RANGE: int+ = number of As to iterate through from A. EX: A = 0, RANGE = 10 would go through a in {0, 1, 2, ..., 9}.
   - PRIMES: int+ = number of primes to iterate through from P. EX: P = 0, PRIMES = 2 would go through {2, 3}.
     Note that the program checks whether a combination of a and p has already been stored in the database so don't worry about
     overlap.
3. In a terminal, run "sage main.py"
