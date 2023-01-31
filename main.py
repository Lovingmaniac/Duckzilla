from code.algorithms.hillclimber import Hillclimber
from code.classes.model import Model
from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output
from code.algorithms.greedy_battery import FillBattery as fb
from code.classes.node import Node
from code.algorithms.breadthfirst import BreadthFirst

from code.algorithms.iteration import Iteration

import math

# from code.algorithms import closest_houses as closest

if __name__ == "__main__":
    # create new grid and model from data
    grid = Grid()

    grid.make_nodes(51)
    grid.load_grid(1)

    model = Model(grid)
    model.add_connections()

    #----------------random assignment of houses to batteries---------------
    # rand.baseline(model, 10000)
    # print(model.nodes)

    battery_model= model.copy()
    rand.run(battery_model)
    visualize(battery_model)
    # # closest.run(model)
    # # print(model.houses)
    # visualize(new_model)
    # new_model = model.copy()
    # print(rand.baseline(new_grid))

    # rand.baseline(model, 10)
    # print(f'score: {rand.get_score(new_mol)}')

    # rand.run(model)
    # output(model)
    # visualize(model)

    #----# -----------greedy_battery--------------------
    # battery_model = model.copy()
    # fillbattery = fb(battery_model)
    # fillbattery.run((0, 0))
    # print(int(math.sqrt(len(model.nodes))))
    # print(battery_model.nodes[(1,1)].get_connections())
    # print(model.nodes[(0,0)].get_type())
    # print(model.batteries)
    #--------------------------------------------------

    #---------------hillclimber random algorithm----------------
    # now randomly tries to improve randomly generated solutions
    # rand.run(model)

    # print(model.calculate_costs())

    # iteration = Iteration(battery_model)
    # iteration.run(1000000)
    # print(battery_model)
    # print(model.total_costs)

    #--------------------------------------------------
    #---------------hillclimber non-random-------------
    
    # hillclimber= Hillclimber(battery_model)
    # hillclimber.run(1000)
    # print(model.total_costs)
    #--------------------------------------------------

    # newest_model = model.copy()
    bf = BreadthFirst(battery_model)
    bf.run()
    
