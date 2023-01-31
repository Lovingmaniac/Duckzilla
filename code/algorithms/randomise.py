import copy
import random
import time
import csv

from code.classes.model import Model
from code.visualization.visualization import visualize


def run(model):
    """Shuffles the list of unconnected houses and then one by one adds this to the batteries
    until these reach max capacity. Then it moves on to the next battery"""

    # Shuffles the unconnected houses
    random.shuffle(model.unconnected_houses)
    random.shuffle(model.batteries)

    # Iterates over the houses
    for house in model.unconnected_houses:
        # Iterates over the batteries
        for battery in model.batteries:

            # Checks whether the battery has space for the house, and adds it if it does
            if battery.has_space(house):
                battery.add_house(house)
                break

    model.make_cables()
<<<<<<< HEAD
    
    with open(f'output/random/output.csv', 'a', newline= '') as f:
        writer = csv.writer(f)
        writer.writerow('run', 'costs', 'time')
        run(model)
        costs = model.calculate_costs()

        if costs < min_costs:
            min_costs = costs
        if model.is_solution():
            writer.writerow(runs, costs, time)
        else:
            f.write('Not a valid solution\n')
=======
>>>>>>> fcbdacb4459b12badc82fdc4f69b087f501cec8c

def get_score(model):
    """takes the manhattan distance between a battery and a house and adds that to a
    so that there is an indication of the length of the cables"""
    cables = 0
    number_cables = 0
    costs = 0
    for battery in model.batteries:
        costs += 5000
        
        for house in battery.houses:
            distance = model.manhattan_distance(battery.location, house.location)
            cables += distance
            costs += distance * 9
    return costs


def baseline(model: Model, runs):
    """Randomises the connections of the houses 100 times and appends the
    score to scores list"""

    min_costs = 100000
    counter = 0
    timestr = time.strftime("%Y%m%d-%H%M%S")

    with open(f'output/histogram_{timestr}.txt', 'w') as f:
        for i in range(runs):
            base_model = model.copy()
            run(base_model)
            costs = base_model.calculate_costs()

            if costs < min_costs:
                min_costs = costs
                print(min_costs)
                visualize(base_model)
            if base_model.is_solution():
                f.write(f'{costs}\n')
            else:
                f.write('Not a valid solution\n')

            # if i in range(0, runs):
            #     print(costs)
            #     print(f'c: {counter}')
            #     counter += 1

