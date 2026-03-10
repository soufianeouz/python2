def garden_operations():
    print("Testing ValueError...")
    try:
        print(int("abc"))
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print()
    print("Testing ZeroDivisionError...")
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print()
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print()
    print("Testing KeyError...")
    try:
        dic = {"name": "soufiane"}
        print(dic["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print()
    print("Testing multiple errors together...")
    try:
        # we can use any error from the last 4 ones
        print(1 / 0)
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")

    print()


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
