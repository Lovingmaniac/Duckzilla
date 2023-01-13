import copy
import random


class Randomize:
    
    def __init__(self, grid) -> None:
        self.grid = copy.deepcopy(grid)


    def run(self):
        random.shuffle(self.grid.houses)
        for battery in self.grid.batteries:
                house = self.grid.houses.pop()
                while battery.has_space(house) and self.grid.houses:
                    battery.add_house(house)
                    house = self.grid.houses.pop()

