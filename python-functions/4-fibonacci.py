def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < n:
            next_num = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_num)
        return fibonacci_list

# Test cases
print(fibonacci_sequence(0))    # Output: []
print(fibonacci_sequence(1))    # Output: [0]
print(fibonacci_sequence(2))    # Output: [0, 1]
print(fibonacci_sequence(5))    # Output: [0, 1, 1, 2, 3]
print(fibonacci_sequence(10))   # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

