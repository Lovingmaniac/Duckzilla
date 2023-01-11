import json
from battery import Battery
from grid import Grid
from house import House


def output(grid):

    # get district info
    district_info = {
        "district": grid.district,
        "costs-shared": 10198
    }

    # initialize list of dictionaries
    output = [district_info]

    for battery in grid.batteries:
        houses = []
        for house in battery.houses:
            house_info = {
                "location": house.get_location(), 
                "output": house.get_output(), 
                "cables": house.get_cables()
            }
            houses.append(house_info)

        battery_info = {
            "location": battery.get_location(), 
            "capacity": battery.capacity, 
            "houses": houses
        }
        output.append(battery_info)

    # write to file with correct indentation
    with open("test_output.json", "w") as write_file:
        json.dump(output, write_file, indent=2)
