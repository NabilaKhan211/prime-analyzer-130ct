# Prime Number Analyzer

**Veda Technology: Python Programming Track · Level 1 · Task 13 (Day 13)**

A program that checks whether a number is prime and generates all prime numbers within a specified range.

## Features
- Reusable `is_prime()` function
- Prime-number range generator (using `is_prime()`)
- Faster range generator using the Sieve of Eratosthenes
- Speed comparison between the two methods
- Handles edge cases: 0, 1, negative numbers, 2, and invalid input
- Shows the reason (a divisor) when a number is not prime

## Requirements
Python 3.6+ (standard library only)

## How to Run
```bash
python prime_analyzer.py
```

## Menu
```
1. Check if a number is prime
2. Generate primes in a range
3. Generate primes in a range (Sieve, faster)
4. Compare speed of both methods
5. Exit
```

## Sample Output
```
Enter a number: 91
91 is NOT a prime number: it is divisible by 7 (91 = 7 x 13).

Primes between 10 and 30: [11, 13, 17, 19, 23, 29]
Count: 6
```

## Algorithm Explanation
**`is_prime(n)`**
1. If `n < 2` → not prime (covers 0, 1, negatives).
2. If `n` is 2 or 3 → prime.
3. If `n` is divisible by 2 or 3 → not prime.
4. Check divisors `i` and `i + 2` starting at 5, increasing `i` by 6 (all primes above 3 are of the form 6k ± 1).
5. Stop when `i * i > n`, since any factor larger than √n pairs with one smaller than √n.

**Sieve of Eratosthenes**
1. Make a list of True flags for 0..end; mark 0 and 1 False.
2. For each prime `i` up to √end, mark its multiples (starting at `i*i`) as False.
3. Numbers still True are prime.

## Complexity
| Method | Time complexity |
|---|---|
| Naive check (all numbers up to n-1) | O(n) per number |
| `is_prime()` with √n and 6k ± 1 | O(√n) per number |
| Sieve of Eratosthenes (whole range) | O(n log log n) |

## Author
Nabila, Veda Technology Intern