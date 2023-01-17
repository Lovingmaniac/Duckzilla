import copy
import random


def make_new_grid(grid):
    '''take the grid and make a deep copy and return this'''
    new_grid = copy.deepcopy(grid)
    return new_grid

def run(grid):
    '''Shuffles the list of unconnected houses and then one by one adds this to the batteries
    until these reach max capacity. Then it moves on to the next battery'''

    # Shuffles the unconnected houses
    random.shuffle(grid.unconnected_houses)

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
    '''takes teh manhattan distance between a battery and a house and adds that to a
    so that there is an indication of the length of the cables'''
    cables = 0
    number_cables = 0
    for battery in grid.batteries:
        for house in battery.houses:
            distance = grid.manhattan_distance(battery.location, house.location)
            cables += distance
            number_cables += len(house.cables)
    return cables

def baseline(grid):
    scores = []
    for i in range(100):
        base_grid = copy.deepcopy(grid)
        run(base_grid)
        scores.append(get_score(base_grid))
    return scores

