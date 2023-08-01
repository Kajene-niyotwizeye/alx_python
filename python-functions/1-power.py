def pow(a, b):
    # Handle special cases
    if b == 0:
        return 1
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result

# Test the function
print(pow(2, 3))  # Output: 8
print(pow(5, 0))  # Output: 1
print(pow(3, -2))  # Output: 0.1111111111111111

