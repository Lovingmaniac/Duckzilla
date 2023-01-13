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
        self.district = 0
        self.houses = []
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

            # iterate over each row in csv file
            for row in reader:
                position = row[0]
                capacity = float(row[1])

                # positions are defined in the form "x,y"
                split = position.split(",")
                x = int(split[0])
                y = int(split[1])

                # make class Battery object and add it to battery list
                self.batteries.append(Battery(x, y, capacity))

                # set node object type as batteryg
                self.nodes[(x, y)].type = "battery"

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

                # make a class House object and add it to house list
                self.houses.append(House(x, y, maxoutput))

                # set node object type to house
                self.nodes[(x, y)].add_type("house")
            
    # def is_solution(self):
    #     for node in self.nodes:
    #         if node.get_type() == "house":
                            
    #             pass