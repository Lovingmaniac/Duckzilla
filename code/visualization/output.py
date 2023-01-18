import json

from code.classes.battery import Battery
from code.classes.grid import Grid
from code.classes.house import House


def output(grid):
    """This function ...."""
    # get district info
    district_info = {"district": grid.district, "costs-shared": grid.calculate_costs()}

    # initialize list of dictionaries
    output = [district_info]

    # initialize list of houses for each battery
    for battery in grid.batteries:
        houses = []

        # initialize house variables to dictionary
        for house in battery.houses:
            house_info = {
                "location": house.get_location(),
                "output": house.get_output(),
                "cables": house.get_cables(),
            }

            # add house dictionary to battery's list of houses
            houses.append(house_info)

        # get battery info as dictionary
        battery_info = {
            "location": battery.get_location(),
            "capacity": battery.capacity,
            "houses": houses,
        }

        # add battery info to output list
        output.append(battery_info)

    # write to file with correct indentation
    with open("output/output.json", "w") as write_file:
        json.dump(output, write_file, indent=2)
