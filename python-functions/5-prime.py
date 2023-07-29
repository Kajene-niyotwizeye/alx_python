def is_prime(number):
    # 1 and any negative number are not prime
    if number < 2:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Even numbers greater than 2 are not prime
    if number % 2 == 0:
        return False

    # Check for divisors from 3 up to the square root of the number
    # We can skip even numbers since they won't divide an odd number evenly
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True

# Test the function
print(is_prime(2))     # True
print(is_prime(3))     # True
print(is_prime(5))     # True
print(is_prime(7))     # True
print(is_prime(11))    # True
print(is_prime(4))     # False
print(is_prime(9))     # False
print(is_prime(15))    # False
print(is_prime(27))    # False
print(is_prime(29))    # True

