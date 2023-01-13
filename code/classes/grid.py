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
        self.houses: list["House"] = []
        self.batteries = []

    def make_grid(self) -> None:
        """"""
        uid = 0

        # iterate over each column
        for x in range(4):
            # iterate over each row
            for y in range(4):
                # create a new node and update uid
                node = Node(x, y, uid)
                uid += 1

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

                self.batteries.append(Battery(x, y, capacity))

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

