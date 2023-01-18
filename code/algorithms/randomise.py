import copy
import random


from code.classes.model import Model


def run(model):
    """Shuffles the list of unconnected houses and then one by one adds this to the batteries
    until these reach max capacity. Then it moves on to the next battery"""

    # Shuffles the unconnected houses
    random.shuffle(model.unconnected_houses)

    # iterate over all the batteries
    for battery in model.batteries:

        # take the last house in the list
        house = model.unconnected_houses.pop()

        # checks wether the battery still has capacity and if there are houses left
        while battery.has_space(house) and model.unconnected_houses:
            battery.add_house(house)
            house = model.unconnected_houses.pop()
    model.make_cables()


def get_score(model):
    """takes the manhattan distance between a battery and a house and adds that to a
    so that there is an indication of the length of the cables"""
    cables = 0
    number_cables = 0
    for battery in model.batteries:
        for house in battery.houses:
            distance = model.manhattan_distance(battery.location, house.location)
            cables += distance
            number_cables += len(house.cables)
    return cables


def baseline(model):
    """Randomises the connections of the houses 100 times and appends the
    score to scores list"""

    with open('data/output/histogram.txt', 'w') as f:
        for i in range(100):
            base_grid = copy.deepcopy(model)
            run(base_grid)
        
            f.write(f'{base_grid.total_costs}\n')
