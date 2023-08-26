#########################################################################################
#                                    Exercise 2
#########################################################################################

def is_all_prime_number(num):
    """Returns True if n is a prime; else, False."""
    # Chunk of code to heck for special cases
    if num <= 1:
        return False
    elif num <= 3:
        return True
    # Check if whether num is divisible by 2 or 3
    elif num % 2 == 0 or num % 3 == 0:
        return False
    # Checking for other numbers divisors up to sqrt(n)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_all_non_primes(a, b):
    """List of all non-prime numbers between a and b is returned (inclusive)"""
    # Swap a and b if a > b
    if a > b:
        a, b = b, a
    # Empty List used for all non prime numbers
    non_primes = []
    # Checking each number between a and b
    for n in range(a, b + 1):
        # If n is not prime, add it to the list
        if not is_all_prime_number(n):
            non_primes.append(n)
    return non_primes

    # Get input from user and check validity
while True:
    try:
            # Get two integers from user
        x1 = int(input("Enter first positive integer: "))
        x2 = int(input("Enter second positive integer: "))
            # Check that both integers are positive
        if x1 <= 0 or x2 <= 0:
            print("Both integers must be positive")
        else:
                # Exit loop if input is valid
            break
    except ValueError:
        print("Invalid input, please enter integers only")

    # Get list of non-primes and output 10 per line
non_primes = get_all_non_primes(x1, x2)
print("All non-prime numbers between "+str(x1)+" and "+str(x2))
for i in range(0, len(non_primes), 10):
  # Output each sublist of 10 non-primes on a separate line
    print(*non_primes[i:i + 10])
