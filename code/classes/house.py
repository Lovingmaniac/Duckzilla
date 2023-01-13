class House:
    def __init__(self, x: int, y: int, output: float) -> None:
        """Constructor of class House
        self.location -- the x-y coordinates of given house
        self.output -- the amount of energy outputted by house
        self.cables -- a list of cables connected to house"""
        self.location = (x, y)
        self.output = output
        self.cables = [tuple]

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

    def get_location(self):
        """Returns the x-y coordinations of given house."""
        return f"{self.location[0]},{self.location[1]}"

    # def get_cables(self) -> list[tuple]:
    #     """Returns the cables connected to house."""
    #     return self.cables

    def __repr__(self) -> str:
        """Returns the correct representation for house class."""
        return f"loc: {self.location}, output: {self.output}"
