def garden_operations(temp_str: str) -> None:
    try:
        tmp = int(temp_str)
        if tmp >= 0 and tmp <= 40:
            print(f"Temperature {tmp}°C is perfect for plants!")
            print()
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
            print()
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
            print()
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        print()


def test_error_types() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    mylist = ["25", "abc", "100", "-50"]
    for temp in mylist:
        print("Testing temperature:", temp)
        garden_operations(temp)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()
