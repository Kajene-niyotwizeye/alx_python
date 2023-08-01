def raise_exception_msg(message=""):
    class NameException(Exception):
        pass

    raise NameException(message)

# Example usage:
try:
    raise_exception_msg("This is a custom exception message.")
except NameException as e:
    print("Caught custom exception:", str(e))
