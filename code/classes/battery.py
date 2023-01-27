from .house import House
from collections import namedtuple


class Battery:
    def __init__(self, x: int, y: int, capacity: float, uid: int) -> None:
        """Constructor of battery
        self.location -- x-y coordinates of battery in tuple
        self.capacity -- the total capacity of energy for battery
        self.current_capacity -- the remaining capacity for battery left
        self.houses -- a list of houses that are connected to the battery"""
        self.location = namedtuple("location", "x y")(x, y)
        self.capacity = capacity
        self.current_capacity = capacity
        self.houses: list[House] = []
        self.id = uid

    def __repr__(self):
        return f"battery: loc:{self.location}, cap:{self.current_capacity}"

    def add_house(self, house: House) -> None:
        """Adds a house to self, sets house to "connected"
        and updates current capacity."""
        # add house to house list
        self.houses.append(house)

        # set house to "connected"
        house.set_connected()

        # update battery capacity
        self.current_capacity -= house.get_output()

    def remove_house(self, house: House) -> None:
        """Removes a house from battery and updates current capacity."""
        self.houses.remove(house)
        self.current_capacity += house.get_output()

    def get_capacity(self) -> float:
        """Returns the remaining capacity of the battery."""
        return self.current_capacity

    def get_location(self):
        """Returns the x-y coordinations of given house."""
        return f"{self.location[0]},{self.location[1]}"

    def has_space(self, house: House) -> bool:
        """Returns true if the battery has sufficient space for a house
        else returns false."""
        return self.current_capacity > house.get_output()
