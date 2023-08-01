import sys

def print_arguments(argv):
    num_args = len(argv)

    print(f"Number of argument(s): {num_args}", end="")
    if num_args == 0:
        print(".", end="")
    elif num_args == 1:
        print(f", followed by: {argv[0]}\n1: {argv[0]}")
    else:
        print(":", end="")
        for i, arg in enumerate(argv):
            print(f"\n{i + 1}: {arg}")

if __name__ == "__main__":
    args = sys.argv[1:]  # Excluding the script name from arguments
    print_arguments(args)
