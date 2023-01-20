from collections import namedtuple


class House:
    def __init__(self, x: int, y: int, output: float) -> None:
        """Constructor of class House
        self.location -- the x-y coordinates of given house
        self.output -- the amount of energy outputted by house
        self.cables -- a list of cables connected to house"""

        self.location = namedtuple("location", "x y")(x, y)    
        self.output = output
        self.cables = []

    def add_cable(self, location: tuple) -> None:
        """Adds a cable to the house object."""

        self.cables.append(location)

    def remove_cable(self, location: tuple) -> None:
        """Removes cable from house object if it is there."""

        # only remove cable if possible
        if location not in self.cables:
            return 1

        # remove cable
        self.cables.remove(location)

    def get_output(self) -> float:
        """Returns the output of a house object."""

        return self.output

    def get_location(self) -> str:
        """Returns the x-y coordinations of given house."""

        return f"{self.location[0]},{self.location[1]}"

    def set_connected(self) -> None:
        """Sets house to connected when it is connected to a battery."""

        self.is_connected = True

    def get_cables(self) -> list:
        """Returns the cables connected to house."""

        return [f"{cable[0]},{cable[1]}" for cable in self.cables]

    def __repr__(self) -> str:
        """Returns the correct representation for house class."""

        return f"house: loc: {self.location}, output: {self.output}"
