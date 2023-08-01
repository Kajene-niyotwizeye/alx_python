class Square:
    def __init__(self, size):
        self.__size = size

# Example usage:
square = Square(5)
print(square.__size)  # This will raise an AttributeError, as __size is private

