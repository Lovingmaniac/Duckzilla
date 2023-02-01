
import math
import argparse
import time


from code.algorithms.hillclimber import Hillclimber
from code.classes.model import Model
from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output
from code.algorithms.greedy_battery import FillBattery as fb
from code.classes.node import Node
from code.algorithms.breadthfirst import BreadthFirst
from code.algorithms.iteration import Iteration, IterationBF


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--random", help="runs random algorithm for X seconds, paths are 90 degrees", type=int)

    parser.add_argument("--random_bf", help="runs random algorithm for X seconds over greedy algorithm, paths are made with breadth first algorithm", type=int)

    parser.add_argument("--random_iteration",  help="runs random hillclimber (iteration) over random algorithm for X seconds, paths are 90 degrees", type=int)

    parser.add_argument("--random_iteration_bf",  help="runs random hillclimber (iteration) over random algorithm for X seconds, paths are made with breadth first algorithm", type=int)

    parser.add_argument("-g", "--greedy", help="runs greedy algorithm once, paths are 90 degrees", type=int)

    parser.add_argument("--greedy_bf", help="runs greedy algorithm once, paths are made with breadth first algorithm", type=int)

    parser.add_argument("-gi", "--greedy_iteration", help="runs iteration algorithm for X seconds over greedy algorithm that is performed once, paths are 90 degrees", type=int)

    parser.add_argument("--greedy_iteration_bf", help="runs iteration algorithm for X seconds over greedy algorithm that is performed once, paths are made using breadthfirst algorithm", type=int)

    args = parser.parse_args()

    # make grid and model objects in first iteration
    start_time = time.time()
    grid = Grid()
    grid.make_nodes(51)
    grid.load_grid(1)
    model = Model(grid)
    model.add_connections()
    it_count = 0

    # run randomise with simple 90 degree cables
    if args.random:
        run_no = 0
        while time.time() - start_time < args.random:
            run_no += 1
            new_model = model.copy()
            rand.run(new_model, run_no, start_time)
            print(new_model.calculate_costs())

    # run randomise for X seconds, then make cables using breadthfirst
    elif args.random_bf:
        run_no = 0
        while time.time() - start_time < args.random_bf:
            run_no += 1
            new_model = model.copy()
            rand.run(new_model, run_no, start_time)
        bf = BreadthFirst(new_model)
        bf.run()
        print(new_model.calculate_costs())

    # runs random once, and improves it until time is over,
    # cables are made 90 degrees in iteration algorithm
    elif args.random_iteration:
        new_model = model.copy()
        rand.run(new_model, 1, 1)
        new_model.houses = model.houses
        iteration = Iteration(new_model)
        iteration.run(max_runtime=args.random_iteration)
        visualize(new_model)
        output(new_model)

    # runs random once, and improves it until time is over,
    # then cables are made using breadth first algorithm
    elif args.random_iteration_bf:
        new_model = model.copy()
        rand.run(new_model, 1, 1)
        new_model.houses = model.houses
        iteration = Iteration(new_model)
        iteration.run(max_runtime=args.random_iteration_bf)
        bf = BreadthFirst(new_model)
        bf.run()

    # runs greedy algorithm once
    elif args.greedy:
        fillbattery = fb(model)
        fillbattery.run((0, 0))

    # runs greedy algorithm once then optimalizes cables using breadthfirst
    elif args.greedy_bf:
        fillbattery = fb(model)
        fillbattery.run((0, 0))
        bf = BreadthFirst(model)
        bf.run()

    # runs greedy algorithm once, then runs hillclimber algorithm on for X seconds, paths are made 90 degrees
    elif args.greedy_iteration:
        fillbattery = fb(model)
        fillbattery.run((0, 0))
        iteration = Iteration(model)
        iteration.run(max_runtime=args.greedy_iteration)

    # runs greedy algorithm once,
    # then optimalizes it using iteration algorithm for X seconds
    # then optimalizes cable structure using breadthfirst
    elif args.greedy_iteration_bf:
        fillbattery = fb(model)
        fillbattery.run((0, 0))
        iteration = Iteration(model)
        iteration.run(max_runtime=args.greedy_iteration_bf)
        bf = BreadthFirst(model)
        bf.run()
