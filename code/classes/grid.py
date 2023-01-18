import csv
import copy

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
        #self.unconnected_houses = []
        self.batteries = []
        self.nodes = {}
        #self.total_costs = 0

    def make_nodes(self) -> None:
        """Create all nodes for grid."""
        uid = 0

        # iterate over each column
        for x in range(51):

            # iterate over each row
            for y in range(51):

                # create a new node and update uid
                node = Node(x, y)
                uid += 1

                # add node to nodes dictionary
                self.nodes[(x, y)] = node

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

                # set node object type to house
                self.nodes[(x, y)].add_type(house)
