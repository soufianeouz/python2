def check_temperature(temp_str: str) -> None:
    try:
        tmp = int(temp_str)
        if tmp >= 0 and tmp <= 40:
            print(f"Temperature {tmp}°C is perfect for plants!")
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    mylist = ["25", "abc", "100", "-50"]
    for temp in mylist:
        print("Testing temperature:", temp)
        check_temperature(temp)
    print("All tests completed - program didn't crash!")