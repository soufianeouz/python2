class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def testing_func() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)

    print()
    try:
        print("Testing WaterError...")
        raise WaterError(" Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)

    print()
    try:
        print("Testing catching all garden errors...")
        raise PlantError(" The tomato plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise WaterError(" Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    testing_func()