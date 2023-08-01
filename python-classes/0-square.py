class Square:
    def __init__(self, size):
        self.__size = size

# Example usage:
square = Square(5)
# This will raise an AttributeError because __size is private
print(square.__size)

