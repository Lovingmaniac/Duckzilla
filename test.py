import json
from battery import Battery
from grid import Grid
from house import House


district = 1

grid = Grid()
grid.load_grid(district)

# add houses to batteries
for battery in grid.batteries:
    # add 2 houses to each battery
    for i in range(2):
        house_to_add = grid.houses.pop()
        battery.add_house(house_to_add)
    
# get district info
district_info = {
    "district": district,
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
            "cables": ["33, 7", "33,8"]
        }
        houses.append(house_info)

    battery_info = {
        "location": battery.get_location(), 
        "capacity": battery.capacity, 
        "houses": houses
    }
    output.append(battery_info)



with open("test_output.json", "w") as write_file:
    json.dump(output, write_file, indent=2)
