import copy

from .battery import Battery
from .grid import Grid
from .house import House
from .node import Node


class Model:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.batteries: list[Battery] = grid.batteries
        self.houses: list[House] = grid.houses
        self.nodes = grid.nodes
        self.unconnected_houses = grid.houses
        self.total_costs = 0
        self.district = grid.district

    def add_connections(self) -> None:
        """Adds all connected nodes as connections to all nodes"""
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # iterate over each node in grid
        for node in self.nodes:

            # iterate over all directions and define x-y coordinates
            for direction in directions:
                connection = (node[0] + direction[0], node[1] + direction[1])

                # add connection to node if possible
                if connection in self.nodes:
                    self.nodes[node].add_connection(connection)

    def calculate_costs(self) -> None:
        """Calculates the total costs for district."""
        # iterate over all batteries
        total_costs = 0
        for battery in self.batteries:
            total_costs += 5000

            # iterate over all houses connected to battery
            for house in battery.houses:
                # get total costs for house and add it to the total costs
                total_costs += ((len(house.cables) - 1) * 9)
        self.total_costs = total_costs
        return total_costs

    # Calculating Manhattan Distance from Scratch
    def manhattan_distance(self, point1, point2):
        distance = 0
        for x1, x2 in zip(point1, point2):
            difference = x2 - x1
            absolute_difference = abs(difference)
            distance += absolute_difference
            # print(distance)

        return distance

    # moet nog aangepast worden
    def is_solution(self) -> bool:
        """Returns True if all houses are connected to a battery, False otherwise."""

        # iterate over all nodes in grid
        for house in self.houses:
            if not house.is_connected:
                return False
        
        # success
        return True

    def make_cables(self):
        """generates cables between house and battery, first moves horizontally
        and then vertically"""

        # iterates over the batteries
        for battery in self.batteries:

            # iterates over the houses in the batteries
            for house in battery.houses:

                # variables for location house and batteries
                x_house, y_house = house.location
                x_battery, y_battery = battery.location

                # add first cable point to house
                house.add_cable((x_house, y_house))

                # set step for x and y direction
                x_step = 1 if x_house < x_battery else -1
                y_step = 1 if y_house < y_battery else -1

                # add x- step and x-cable point to house
                while not x_house == x_battery:
                    x_house += x_step
                    house.add_cable((x_house, y_house))

                # add y-step and y-cable point to house
                while not y_house == y_battery:
                    y_house += y_step
                    house.add_cable((x_house, y_house))

                # set house to "connected"
                house.set_connected()

    def copy(self) -> 'Model':
        """Returns shallow copy of all grid and costs score."""

        # make shallow copy of model
        new_model = copy.deepcopy(self)

        # only copy the attributes needed for algorithms
        # new_model.unconnected_houses = copy.copy(self.unconnected_houses)
        # new_model.total_costs = copy.copy(self.total_costs)

        return new_model
