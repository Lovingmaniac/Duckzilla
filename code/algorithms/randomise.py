import copy
import random


from code.classes.model import Model


def run(model):
    """Shuffles the list of unconnected houses and then one by one adds this to the batteries
    until these reach max capacity. Then it moves on to the next battery"""

    # Shuffles the unconnected houses
<<<<<<< HEAD
    random.shuffle(model.unconnected_houses)
=======
    random.shuffle(grid.unconnected_houses)
    random.shuffle(grid.batteries)
>>>>>>> c24a4b0f9d52bd98a42a10a5d3eab7156614cccd

    # iterate over all the batteries
    for battery in model.batteries:

        # take the last house in the list
<<<<<<< HEAD
        house = model.unconnected_houses.pop()
=======
        house = grid.unconnected_houses.pop()
        
>>>>>>> c24a4b0f9d52bd98a42a10a5d3eab7156614cccd

        # checks wether the battery still has capacity and if there are houses left
        while battery.has_space(house) and model.unconnected_houses:
            battery.add_house(house)
<<<<<<< HEAD
            house = model.unconnected_houses.pop()
    model.make_cables()
=======
            house = grid.unconnected_houses.pop()

    grid.make_cables()
>>>>>>> c24a4b0f9d52bd98a42a10a5d3eab7156614cccd


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

<<<<<<< HEAD

def baseline(model):
    """Randomises the connections of the houses 100 times and appends the
    score to scores list"""

    with open('data/output/histogram.txt', 'w') as f:
        for i in range(100):
            base_grid = copy.deepcopy(model)
            run(base_grid)
        
            f.write(f'{base_grid.total_costs}\n')
=======
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
>>>>>>> c24a4b0f9d52bd98a42a10a5d3eab7156614cccd
