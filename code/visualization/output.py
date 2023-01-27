import json
import time

from code.classes.battery import Battery
from code.classes.grid import Grid
from code.classes.house import House


def output(model):
    """This function ...."""
    # get district info
    timestr = time.strftime("%Y%m%d-%H%M%S")
    district_info = {"district": model.district, "costs-shared": model.calculate_costs()}

    # initialize list of dictionaries
    output = [district_info]

    # initialize list of houses for each battery
    for battery in model.batteries:
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
    with open(f"output/output_{timestr}.json", "w") as write_file:
        json.dump(output, write_file, indent=2)
