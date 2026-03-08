"""Garden temperature checker.

Flake8/PEP8 cleanup only (no logic changes).
"""

def check_temperature(temp_str: str):
    """Parse a temperature from string and print garden-friendly messages."""
    try:
        tmp = int(temp_str)
        if 0 <= tmp <= 40:
            print(f"Temperature {tmp}°C is perfect for plants!")
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """Run basic tests for check_temperature."""
    print("=== Garden Temperature Checker ===")
    mylist = ["25", "abc", "100", "-50"]
    for temp in mylist:
        print("Testing temperature:", temp)
        check_temperature(temp)
    print("All tests completed - program didn't crash!")


test_temperature_input()