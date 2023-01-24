from code.classes.model import Model
from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output
from code.algorithms.greedy_battery import FillBattery as fb

from code.algorithms.iteration import Iteration

import math

# from code.algorithms import closest_houses as closest

if __name__ == "__main__":
    # create new grid and model from data
    grid = Grid()
    grid.make_nodes(50)
    grid.load_grid(1)

    model = Model(grid)
    
    #----------------random assignment of houses to batteries---------------
    # rand.baseline(model, 1)
    # print(model.nodes)

    # rand.run(model)
    # closest.run(model)
    # print(model.houses)
    # visualize(model)
    # new_model = model.copy()
    # print(rand.baseline(new_grid))
    
    # rand.baseline(model, 10)
    # print(f'score: {rand.get_score(new_mol)}')
    
    # rand.run(model)
    # output(model)
    # visualize(model)

    #---------------greedy_battery--------------------
    battery_model = model.copy()
    fillbattery = fb(battery_model)
    fillbattery.run((0,0))
    # print(int(math.sqrt(len(model.nodes))))
    # print(model.nodes[(0,0)].get_type())
    # print(model.batteries)
    #--------------------------------------------------

    #---------------iteration algorithm----------------
    # now randomly tries to improve randomly generated solutions
    rand.run(model)


    # but could use another searching algorithm for future?

    iteration = Iteration(model)
    iteration.run(100)
    print(model.total_costs)

    #--------------------------------------------------
