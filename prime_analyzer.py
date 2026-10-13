"""Prime Number Analyzer.

Features:
    1. Check whether a number is prime (reusable is_prime() function)
    2. Generate all primes in a range (using is_prime)
    3. Fast range generation using the Sieve of Eratosthenes
    4. Compare the speed of both methods
"""
import time


def is_prime(n):
    """Return True if n is prime.

    Optimizations (avoid unnecessary divisibility checks):
      * numbers below 2 are not prime (handles 0, 1, negatives)
      * 2 and 3 are prime; multiples of 2 or 3 are not
      * every other prime has the form 6k +/- 1, so test only i and i + 2
        in steps of 6
      * stop at sqrt(n), because a larger factor would pair with a smaller one
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_in_range(start, end):
    """Return all primes in [start, end] by calling is_prime() on each number."""
    return [n for n in range(max(start, 2), end + 1) if is_prime(n)]


def sieve_primes(start, end):
    """Return all primes in [start, end] using the Sieve of Eratosthenes."""
    if end < 2:
        return []
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, end + 1, i):
                sieve[multiple] = False
    return [n for n in range(max(start, 2), end + 1) if sieve[n]]


def read_int(prompt):
    """Read an integer from the user, returning None if invalid."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return None


def check_number():
    n = read_int("Enter a number: ")
    if n is None:
        return
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        if n < 2:
            reason = "prime numbers must be greater than 1"
        else:
            d = next(i for i in range(2, n) if n % i == 0)
            reason = f"it is divisible by {d} ({n} = {d} x {n // d})"
        print(f"{n} is NOT a prime number: {reason}.")


def get_range():
    start = read_int("Enter start of range: ")
    end = read_int("Enter end of range: ") if start is not None else None
    if start is None or end is None:
        return None
    if start > end:
        print("Start cannot be greater than end.")
        return None
    return start, end


def show_primes(primes, start, end):
    if not primes:
        print(f"No prime numbers between {start} and {end}.")
        return
    print(f"Primes between {start} and {end}: {primes}")
    print(f"Count: {len(primes)}")


def generate_range():
    r = get_range()
    if r:
        show_primes(primes_in_range(*r), *r)


def generate_sieve():
    r = get_range()
    if r:
        show_primes(sieve_primes(*r), *r)


def compare_speed():
    limit = read_int("Compare speed for primes up to (e.g. 100000): ")
    if limit is None:
        return
    t = time.perf_counter()
    a = primes_in_range(2, limit)
    t1 = time.perf_counter() - t
    t = time.perf_counter()
    b = sieve_primes(2, limit)
    t2 = time.perf_counter() - t
    print(f"is_prime() method : {len(a)} primes in {t1:.4f} s")
    print(f"Sieve method      : {len(b)} primes in {t2:.4f} s")
    print("Both methods give the same result." if a == b else "Results differ!")


MENU = """
====== PRIME NUMBER ANALYZER ======
1. Check if a number is prime
2. Generate primes in a range
3. Generate primes in a range (Sieve, faster)
4. Compare speed of both methods
5. Exit
===================================
"""
ACTIONS = {"1": check_number, "2": generate_range, "3": generate_sieve, "4": compare_speed}


def main():
    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()