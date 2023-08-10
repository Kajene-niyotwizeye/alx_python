class BaseGeometry:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

# Example usage
try:
    rectangle = Rectangle(10, 5)
    print("Rectangle created successfully!")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

