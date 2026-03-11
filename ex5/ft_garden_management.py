class PlantError(Exception):
    pass


class GardenError(Exception):
    pass


class GardenManager():

    def __init__(self) -> None:
        self.plants = []

    def add_plants(self, plant_name: str, water_level: int,
                   sunlight_hours: int) -> None:
        try:
            if plant_name == "" or plant_name is None:
                raise PlantError("Plant name cannot be empty or None!")
            for i in self.plants:
                if i["plant_name"] == plant_name:
                    raise PlantError("Plant is already added!")
            plant_info = {"plant_name": plant_name, "water_level": water_level,
                          "sunlight_hours": sunlight_hours}
            self.plants.append(plant_info)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print("Error adding plant:", e)

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant['plant_name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant["water_level"] < 1:
                    raise PlantError(f"Water level {plant['water_level']} "
                                     f"is too low (min 1)")
                if plant["water_level"] > 10:
                    raise PlantError(f"Water level {plant['water_level']} "
                                     f"is too high (max 10)")

                if plant["sunlight_hours"] < 2:
                    raise PlantError(f"sunlight hours "
                                     f"{plant['sunlight_hours']} "
                                     f"is too low (min 2)")
                if plant["sunlight_hours"] > 12:
                    raise PlantError(f"sunlight hours "
                                     f"{plant['sunlight_hours']}"
                                     f" is too high (max 12)")
                print(f"{plant['plant_name']}: healthy (water: "
                      f"{plant['water_level']}, "
                      f"sun: {plant['sunlight_hours']})")
            except PlantError as e:
                print(f"Error checking {plant['plant_name']}:", e)


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    objtest = GardenManager()
    objtest.add_plants("tomato", 5, 8)
    objtest.add_plants("lettuce", 15, 6)
    objtest.add_plants("", 5, 3)
    print()

    print("Watering plants...")
    objtest.water_plants()
    print()
    objtest.check_plant_health()
    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
