import csv

from .battery import Battery
from .house import House
from .node import Node



class Grid:
    def __init__(self) -> None:
        """Constructor of class Grid
        self.district -- the district info
        self.houses -- list of all houses in grid
        self.batteries -- list of all batteries in grid"""
        self.district = 1
        self.houses = []
        self.unconnected_houses = []
        self.batteries = []
        self.nodes = {}

    def make_nodes(self) -> None:
        """Create all nodes for grid."""
        uid = 0

        # iterate over each column
        for x in range(51):

            # iterate over each row
            for y in range(51):

                # create a new node and update uid
                node = Node(x, y, uid)
                uid += 1

                # add node to nodes dictionary
                self.nodes[(x, y)] = node

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
                    self.nodes[(node)].add_connection(connection)

    def load_grid(self, district) -> None:
        """Loads grid for district."""
        self.district = district

        # load battery data
        with open(
            f"data/district_{district}/district-{district}_batteries.csv"
        ) as csvfile:
            reader = csv.reader(csvfile)

            # skip the header
            next(reader, None)
            uid = 1

            # iterate over each row in csv file
            for row in reader:
                position = row[0]
                capacity = float(row[1])

                # positions are defined in the form "x,y"
                split = position.split(",")
                x = int(split[0])
                y = int(split[1])

                # make a new Battery object
                battery = Battery(x, y, capacity, uid)

                # make class Battery object and add it to battery list
                self.batteries.append(battery)

                # set node object type as battery
                self.nodes[(x, y)].type = battery

                # make new id number
                uid += 1

        # load houses data
        with open(
            f"data/district_{district}/district-{district}_houses.csv"
        ) as csvfile:
            reader = csv.reader(csvfile)

            # skip the header
            next(reader, None)

            # iterate over each row in csv file
            for row in reader:
                x = int(row[0])
                y = int(row[1])
                maxoutput = float(row[2])

                # make a new House object
                house = House(x, y, maxoutput)

                # make a class House object and add it to house list
                self.houses.append(house)
                self.unconnected_houses.append(house)

                # set node object type to house
                self.nodes[(x, y)].add_type(house)

    def calculate_costs(self):
        for battery in self.batteries:
            pass

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
        for node in self.nodes:

            # find house nodes
            if type(node) == type(House):

                # if it is connected, continue
                if node.is_connected is True:
                    continue

                # if not connected, this is no valid solution
                else:
                    return False

        # success
        return True

    def make_cables(self):
        ''' generates cables between house and battery, first moves horizontally
        and then vertically'''

        # iterates over the batteries
        for battery in self.batteries:

            # iterates over the houses in the batteries
            for house in battery.houses:
                # variables for location house and batteries
                x_house, y_house = house.location
                x_battery, y_battery = battery.location
                
                
                # finds the coordinates for every cable in every quadrant of the battery grid
                x_step = 1 if x_house < x_battery else -1
                y_step = 1 if y_house < y_battery else -1
                while not x_house == x_battery:
                    x_house += x_step
                    house.add_cable((x_house, y_house))
                while not y_house == y_battery:
                    y_house += y_step
                    house.add_cable((x_house, y_house))
