import copy
import random


def make_new_grid(grid):
    """take the grid and make a deep copy and return this"""
    new_grid = copy.deepcopy(grid)
    return new_grid

def run(grid):
    """Shuffles the list of unconnected houses and then one by one adds this to the batteries
    until these reach max capacity. Then it moves on to the next battery"""

    # Shuffles the unconnected houses
    random.shuffle(grid.unconnected_houses)
    random.shuffle(grid.batteries)

    # iterate over all the batteries
    for battery in grid.batteries:

        # take the last house in the list
        house = grid.unconnected_houses.pop()
        

        # checks wether the battery still has capacity and if there are houses left
        while battery.has_space(house) and grid.unconnected_houses:
            battery.add_house(house)
            house = grid.unconnected_houses.pop()

    grid.make_cables()

def get_score(grid):
    """takes the manhattan distance between a battery and a house and adds that to a
    so that there is an indication of the length of the cables"""
    cables = 0
    number_cables = 0
    for battery in grid.batteries:
        for house in battery.houses:
            distance = grid.manhattan_distance(battery.location, house.location)
            cables += distance
            number_cables += len(house.cables)
    return cables

def baseline(grid, new_range):
    """Randomises the connections of the houses 100 times and appends the
    score to scores list"""

    with open('output/histogram.txt', 'w') as f:
        for i in range(new_range):
            base_grid = copy.deepcopy(grid)
            run(base_grid)

            if len(base_grid.unconnected_houses) > 0: 
                f.write('0\n')
            else:
                f.write(f'{base_grid.calculate_costs()}\n')
            
            if i in range(0, new_range, 100):
                print(base_grid.calculate_costs())