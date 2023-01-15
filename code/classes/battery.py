from .house import House


class Battery:
    def __init__(self, x: int, y: int, capacity: float) -> None:
        """Constructor of battery
        self.location -- x-y coordinates of battery in tuple
        self.capacity -- the total capacity of energy for battery
        self.current_capacity -- the remaining capacity for battery left
        self.houses -- a list of houses that are connected to the battery"""
        self.location = (x, y)
        self.capacity = capacity
        self.current_capacity = capacity
        self.houses: list[House] = []

    def __repr__(self):
        return f"loc:{self.location}, cap:{self.current_capacity}"

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
        self.houses.delete(house)
        self.current_capacity += house.getoutput()

    def get_capacity(self) -> float:
        """Returns the remaining capacity of the battery."""
        return self.current_capacity

    def get_location(self):
        """Returns the x-y coordinations of given house."""
        return f"{self.location[0]},{self.location[1]}"

    def has_space(self, house: House) -> bool:
        """Returns true if the battery has sufficient space for a house
        else returns false."""
        # if output of house is more than remaining battery capacity, return False
        if house.get_output() > self.current_capacity:
            return False
            # retun true if output of house is smaller than remaining battery capacy
        else:
            return True
