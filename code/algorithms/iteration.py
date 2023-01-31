import random
import time

from code.classes.model import Model
from code.visualization.visualization import visualize

"""
to do:
- gradient descent
- choose houses per output

- parser:
-- visualise
-- lowest costs
-- counter(rounds)
-- time
"""


class Iteration():
    """Class iteration algorithm
    Class takes a valid solution, and tries to improve it mutating changes for X iterations."""

    def __init__(self, model: Model):
        """Constructor of class Iteration:
        Arguments:
        model -- a model of class Model with valid solution

        Returns:
        self.model -- model object that is a copy of given model
        self.best_costs -- best costs reached in algorithm, starting with solution of given model"""
        if not model.is_solution():
            raise Exception("Please provide a valid solution.")

        self.model = model.copy()
        self.original_costs = model.calculate_costs()
        self.best_costs = 100000

    def mutate_battery_connection(self, new_model: Model):
        """Switches two random existing connections of model. 
        Random batteries are generated, with random houses connected to each battery.
        Houses are swapped, from house lists in batteries. 
        Old cables are removed and new cables are made.

        Arguments:
        new_model -- the model of input with existing connections"""
        # get random batteries
        rand_battery_1 = self.get_rand_battery(new_model)
        rand_battery_2 = self.get_rand_battery(new_model)

        # second random battery has to differ from first one
        while rand_battery_2 == rand_battery_1:
            rand_battery_2 = self.get_rand_battery(new_model)

        # generate random houses
        rand_house_1 = self.get_rand_house(new_model, rand_battery_1)
        rand_house_2 = self.get_rand_house(new_model, rand_battery_2)

        # swap houses from battery lists
        self.swap_houses(rand_battery_1,
                         rand_battery_2,
                         rand_house_1,
                         rand_house_2)

        # remove old cables
        new_model.remove_one_cable(rand_battery_1, rand_house_1)
        new_model.remove_one_cable(rand_battery_2, rand_house_2)

        # # add new cables
        new_model.add_one_cable(rand_battery_1, rand_house_2)
        new_model.add_one_cable(rand_battery_2, rand_house_1)

    def swap_houses(self, battery_1, battery_2, house_1, house_2):
        battery_1.houses.append(house_2)
        battery_2.houses.append(house_1)

        house_1.battery = battery_2
        house_2.battery = battery_1

        idx_house_1 = battery_1.houses.index(house_1)
        del battery_1.houses[idx_house_1]

        idx_house_2 = battery_2.houses.index(house_2)
        del battery_2.houses[idx_house_2]

    def get_rand_house(self, new_model: Model, battery):
        """Returns a random house from a randomly generated battery."""
        idx = random.randint(0, (len(battery.houses) - 1))
        rand_house = battery.houses[idx]
        return rand_house

    def get_rand_battery(self, new_model: Model):
        """Returns a random battery from model's battery list.
        Arguments:
        new_model -- the model of input with existing connections

        Returns:
        rand_battery -- random generated battery object from battery list"""
        idx = random.randint(0, (len(new_model.batteries) - 1))
        rand_battery = new_model.batteries[idx]
        return rand_battery

    def mutate_model(self, new_model: Model) -> None:
        """Changes all batteries randomly to random houses.
        Arguments:
        new_model --the model of input with existing connections"""
        # iterate over all batteries
        for i in range(5):
            self.mutate_battery_connection(new_model)

    def check_solution(self, new_model: Model) -> None:
        """Checks if solution is a better solution than the best solution reached.
        If solution has lower costs and is valid,
        current best costs and model solution are switched to solution model.
        Arguments:
        new_model -- the model of input with existing connections."""
        # try new solution
        new_solution = new_model.calculate_costs()
        old_solution = self.best_costs

        # if the costs are, change current model to new solution
        if new_model.is_solution() is False:
            print("no")
            return None

        if new_solution < old_solution:
            print("found better solution")
            self.best_costs = new_solution
            print(new_solution)
            self.model = new_model
            visualize(self.model)

    def run(self, iterations: int) -> None:
        """Runs the hillclimber algorithm for a specific amount of iterations.
        First a copy is made of current model solution.
        Then a mutation is made of current model solution.
        If mutation model is better and valid, it becomes current best solution.
        Arguments:
        iterations -- the amount of times to run this function"""

        for iteration in range(iterations):
            # make copy of model for mutations
            new_model = self.model.copy()

            # mutate model
            self.mutate_model(new_model)

            # if solution is better and valid, change swap model to mutate model
            self.check_solution(new_model)
            timestr = time.strftime("%Y%m%d-%H%M%S")

            # open the file and append the data
            with open(f'output/iteration/output.txt', 'a') as f:
                if new_model.is_solution():
                    f.write(f'dag/tijd: {timestr}\n costs: {new_model.calculate_costs()}\n\n')
                else:
                    f.write('Not a valid solution\n')
