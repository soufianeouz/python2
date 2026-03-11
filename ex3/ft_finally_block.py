def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    Plant_list = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(Plant_list)
    print("Watering completed successfully!")
    print()
    Plant_list = ["tomato", None, "carrots"]
    print("Testing with error...")
    water_plants(Plant_list)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()