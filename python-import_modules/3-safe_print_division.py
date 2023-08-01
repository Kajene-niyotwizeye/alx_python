def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        print("Inside result: {}".format(result) if 'result' in locals() else "Inside result: None")
        return result

# Test the function with some examples
safe_print_division(10, 2)
safe_print_division(5, 0)
safe_print_division(8, 3)

