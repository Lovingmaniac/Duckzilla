import random

from code.classes.model import Model
from code.visualization.visualization import visualize

"""
to do:

- fix bug in randomise.run(), empty houselist after performance
- make assertion that only solutions are given
- gradient descent

- swap houses
- choose houses per output
-

- parser:
-- visualise
-- lowest costs
-- counter(rounds)
-- time
--
--
"""

class Iteration():
    """Class iteration algorithm
    Class takes a valid solution, and tries to improve it mutating changes for X iterations."""

    def __init__(self, model: Model):
        # if not model.is_solution():
        #     raise Exception("Please provide a valid solution.")

        self.model = model.copy()
        self.original_costs = model.calculate_costs()

    def mutate_battery_connection(self, new_model: Model) -> None:
        """Changes the connection from a random battery to a random house."""
        # generate a random battery and random house connected to battery
        idx_first_battery = self.get_rand_battery_idx(new_model)
        first_battery = self.get_rand_battery(new_model, idx_first_battery)
        first_house = self.get_rand_house(new_model, idx_first_battery)

        # generate another random battery/house connection
        idx_mutate_battery = self.get_rand_battery_idx(new_model)
        mutate_battery = self.get_rand_battery(
            new_model, idx_mutate_battery)

        # only accept a different battery
        while idx_first_battery == idx_mutate_battery:
            idx_mutate_battery = self.get_rand_battery_idx(new_model)

        # generate random house connected to random mutate battery
        mutate_house = self.get_rand_house(new_model, idx_mutate_battery)

        # remove original cables
        new_model.remove_one_cable(first_battery, first_house)
        new_model.remove_one_cable(mutate_battery, mutate_house)

        # add new connections and update capacity of batteries
        new_model.batteries[idx_first_battery].add_house(mutate_house)
        new_model.batteries[idx_mutate_battery].add_house(first_house)

        # remove original connections and update capacity of batteries
        new_model.batteries[idx_first_battery].remove_house(first_house)
        new_model.batteries[idx_mutate_battery].remove_house(mutate_house)

        # add new cables
        new_model.add_one_cable(first_battery, mutate_house)
        new_model.add_one_cable(mutate_battery, first_house)

    def get_rand_house(self, new_model: Model, battery_idx: int):
        """returns a random house"""
        idx_rand_house = random.randint(0, (len(new_model.batteries[battery_idx].houses) - 1))
        rand_house = new_model.batteries[battery_idx].houses[idx_rand_house]
        return rand_house

    def get_rand_battery_idx(self, new_model: Model) -> int:
        """Returns random battery index"""
        idx_rand_battery = random.randint(0, (len(new_model.batteries) - 1))
        return idx_rand_battery

    def get_rand_battery(self, new_model: Model, idx_rand_battery: int):
        rand_battery = new_model.batteries[idx_rand_battery]
        return rand_battery

    def mutate_model(self, new_model: Model) -> None:
        """Changes all batteries randomly to random houses."""
        # iterate over all batteries
        for i in range(5):
            self.mutate_battery_connection(new_model)

    def check_solution(self, new_model: Model) -> None:
        """Checks if solution is a better solution than the best solution reached."""
        # try new solution
        new_solution = new_model.calculate_costs()
        old_solution = self.original_costs

        # if the costs are, change current model to new solution
        if new_model.is_solution() is False:
            print("no")
            return None

        if new_solution < old_solution:
            print("found better solution")
            self.original_costs = new_solution
            print(new_solution)
            self.model = new_model
            visualize(self.model)

    def run(self, iterations: int) -> None:
        """Runs the hillclimber algorithm for a specific amount of iterations."""

        for iteration in range(iterations):
            # print(f"Iteration {iteration}/{iterations}, current_value: {self.total_costs}") if verbose else None

            # make copy of model for mutations
            new_model = self.model.copy()

            # mutate model
            self.mutate_model(new_model)

            # if new_model.calculate_costs() < current_best.calculate_costs():
            #     print("better solution")
            #     current_best = new_model
            # else:
            #     print(f"same{new_model.calculate_costs()} {new_model == current_best}")
            # # set mutation model to cur
            #rent model if more successful than current
            self.check_solution(new_model)
