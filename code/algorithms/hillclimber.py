import time
import csv
import random


from code.classes.model import Model
from code.classes.house import House
from code.classes.battery import Battery


class Iteration():
    """
    Class hillclimber algorithm
    Class takes a valid solution, tries to improve it mutating
    changes for X hillclimbers or X seconds.
    """
    def __init__(self, model: 'Model') -> None:
        """
        Constructor of class Hillclimber:
        Arguments:
        model -- a model of class Model with valid solution

        Returns:
        self.model -- model object that is a copy of given model
        self.best_costs -- best costs reached in algorithm,
        starting with solution of given model
        """
        if not model.is_solution():
            raise Exception("Please provide a valid solution.")

        self.model = model.copy()
        self.best_costs = model.calculate_costs()

    def mutate_battery_connection(self, new_model: 'Model') -> None:
        """
        Switches two  existing house/battery connections in model.
        Random batteries are generated, most expensive houses are
        swapped from both.
        Houses are swapped, from house lists in batteries.
        Old cables are removed and new cables are made.

        Arguments:
        new_model -- the model of input with existing connections
        """
        # get random batteries
        rand_battery_1 = self.get_rand_battery(new_model)
        rand_battery_2 = self.get_rand_battery(new_model)

        # second random battery has to differ from first one
        while rand_battery_2 == rand_battery_1:
            rand_battery_2 = self.get_rand_battery(new_model)

        # get most expensive houses from batteries
        exp_house_1 = self.get_expensive_house(new_model, rand_battery_1)
        exp_house_2 = self.get_expensive_house(new_model, rand_battery_2)

        # swap houses from battery lists
        self.swap_houses(rand_battery_1,
                         rand_battery_2,
                         exp_house_1,
                         exp_house_2)

        # remove old cables
        new_model.remove_one_cable(rand_battery_1, rand_house_1)
        new_model.remove_one_cable(rand_battery_2, rand_house_2)

        # # add new cables
        new_model.add_one_cable(rand_battery_1, rand_house_2)
        new_model.add_one_cable(rand_battery_2, rand_house_1)

    def swap_houses(self,
                    battery_1: 'Battery',
                    battery_2:'Battery',
                    house_1: 'House',
                    house_2: 'House') -> None:
        """Swaps houses from batteries.
        Houses are first added to new batteries, then removed from old battery
        Arguments:
        battery_1 -- battery object from which to swap houses
        battery_2 -- battery object from which to swap houses
        house_1 -- house object to add/remove to old/new battery
        house_2 -- house object to add/remove to old/new battery"""
        # add new houses to new battery's house lists
        battery_1.houses.append(house_2)
        battery_2.houses.append(house_1)

        # new batteries are added to house
        house_1.battery = battery_2
        house_2.battery = battery_1

        # remove old house from battery 1
        idx_house_1 = battery_1.houses.index(house_1)
        del battery_1.houses[idx_house_1]

        # remove old house from battery 2
        idx_house_2 = battery_2.houses.index(house_2)
        del battery_2.houses[idx_house_2]

    def get_expensive_house(self,
                            new_model: 'Model',
                            battery: 'Battery') -> 'House':
        """
        Returns most expensive house from a randomly generated battery.
        Arguments:
        new_model -- copy of original model, from which to mutate
        battery -- random battery from which to pull most expensive house
        """
        most_exp_output = 0
        most_exp_house = None

        # iterate over houses in battery
        for house in battery.houses:
            # get most expensive house
            if house.output > most_exp_output:
                most_exp_house = house
        return most_exp_house

    def get_rand_battery(self, new_model: 'Model'):
        """
        Returns a random battery from model's battery list.
        Arguments:
        new_model -- the model of input with existing connections

        Returns:
        rand_battery -- random generated battery object from battery list
        """
        idx = random.randint(0, (len(new_model.batteries) - 1))
        rand_battery = new_model.batteries[idx]
        return rand_battery

    def mutate_model(self, new_model: 'Model') -> None:
        """
        Changes most expensive houses from batteries.
        Arguments:
        new_model --the model of input with existing connections
        """
        for i in range(5):
            self.mutate_battery_connection(new_model)

    def check_solution(self,
                       new_model: 'Model',
                       it_count: int,
                       it_time: float) -> None:
        """
        Checks if solution is a better than the best solution reached.
        If solution has lower costs and is valid,
        current best costs and model solution are switched to new model.
        Arguments:
        new_model -- the model of input with existing connections
        """
        # try new solution
        new_solution = new_model.calculate_costs()
        old_solution = self.best_costs

        # only accept valid solutions
        if new_model.is_solution() is False:
            return None

        # change current model and best costs to mutated model if cheaper
        # write new best costs in experiment file
        if new_solution < old_solution:
            self.best_costs = new_solution
            self.model = new_model
            self.experiment_file(it_count, self.best_costs, it_time)

    def experiment_file(self,
                        it_count: int,
                        total_costs: int,
                        it_time: float) -> None:
        """
        Writes result of current result in csv file in output directory
        Arguments:
        it_count -- iteration round
        total_costs -- costs result to add in file
        it_time -- time of achieved result after start time
        """
        with open(
                "output/experiment_hillclimber_bf.csv",
                "a",newline="") as result_file:

            # create writer object
            csv_writer = csv.writer(result_file)

            # make list of values for line
            line = [f"iteration: {it_count}",
                    f" total costs: {total_costs}",
                    f" time since start run: {it_time}"]

            # append list to new csv row
            csv_writer.writerow(line)

    def run_algorithm(
            self,
            it_count: int,
            it_time: float) -> None:
        """
        Runs the hillclimber algorithm once.
        First a copy is made of current model solution.
        Then a mutation is made of current model solution.
        If mutation model is better and valid, it becomes current best solution.
        Arguments:
        it_count -- current iteration number
        it_time -- current iteration time since start run
        """

        # print time and iteration count in terminal
        print(f"iteration: {it_count}, time after run: {it_time}")

        # make copy of model for mutations
        new_model = self.model.copy()

        # mutate model
        self.mutate_model(new_model)

        # if solution is better and valid, swap model to mutate model
        self.check_solution(new_model, it_count, it_time)

    def run(self,
            max_runtime: int = None,
            iteration: int = None,
            ) -> None:
        """
        Wrapper around run_algorithm to either exit after N hillclimbers, 
        or after a certain amount of time has passed. 
        """
        # set start time and hillclimber count
        start_time = time.time()
        it_count = 0

        # run for hillclimber amount of hillclimbers
        if hillclimber:
            for it_count in range(hillclimber):
                it_time = time.time() - start_time
                self.run_algorithm(it_count,
                                   it_time)
        elif max_runtime:
            # run hillclimber
            until maximum time
            while time.time() - start_time < max_runtime:
                it_count += 1
                it_time = time.time() - start_time
                self.run_algorithm(it_count,
                                   it_time)
