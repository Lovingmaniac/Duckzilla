import random

from code.classes.model import Model
"""
to do:
- is_solution?
- fix bug in randomise.run(), empty houselist after performance
- make assertion that only solutions are given
- gradient descent

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
        self.total_costs = model.calculate_costs()

    def mutate_battery_connection(self, new_model: Model) -> None:
        """Changes the connection from a random battery to a random house."""

        # generate a random int index for battery
        idx_battery = random.randint(0, (len(new_model.batteries) - 1))

        # generate a random int index for house
        idx_house = random.randint(0, (len(new_model.houses) - 1))

        # connect random battery to random house
        new_model.batteries[idx_battery].add_house(new_model.houses[idx_house])

    def mutate_model(self, new_model: Model) -> None:
        """Changes all batteries randomly to random houses."""
        # iterate over all batteries
        for i in range(5):
            self.mutate_battery_connection(new_model)

    def check_solution(self, new_model: Model) -> None:
        """Checks if solution is a better solution than the best solution reached."""
        # try new solution
        new_solution = new_model.calculate_costs()
        old_solution = self.total_costs

        # if the costs are, change current model to new solution
        if not new_model.is_solution():
            return None

        if new_solution > old_solution:
            self.total_costs = new_solution
            self.model = new_model

    def run(self, iterations: int) -> None:
        """Runs the hillclimber algorithm for a specific amount of iterations."""
        for iteration in range(iterations):
            # print(f"Iteration {iteration}/{iterations}, current_value: {self.total_costs}") if verbose else None

            # make copy of model for mutations
            new_model = self.model.copy()

            # mutate model
            self.mutate_model(new_model)

            # set mutation model to current model if more successful than current
            self.check_solution(new_model)
