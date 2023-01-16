import copy
import random


class Randomize:
    def __init__(self, grid) -> None:
        self.grid = copy.deepcopy(grid)

    def run(self):
        random.shuffle(self.grid.unconnected_houses)
        for battery in self.grid.batteries:
            house = self.grid.unconnected_houses.pop()
            while battery.has_space(house) and self.grid.unconnected_houses:
                battery.add_house(house)
                house = self.grid.unconnected_houses.pop()
        # print(self.grid.batteries)

    def get_score(self):
        
        cables = 0
        for battery in self.grid.batteries:
            for house in self.grid.batteries.houses:
                length = self.grid.manhattan_distance(battery, house)
                cables += length
        return cables



