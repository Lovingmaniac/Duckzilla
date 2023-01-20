import copy
import random
import time
import random
import math

from code.classes.model import Model
from code.visualization.visualization import visualize
from code.classes.house import House

class FillBattery():
    def __init__(self, model: Model):
        self.model = model
        self.nodes = model.nodes
    
    # def close_batteries(self, house):

    #     for battery in model.batteries:
    #         house.location.x 

    def spiral_sort(self, startpoint):
        dimensions = int(math.sqrt(len(self.nodes)))
        rows, cols = dimensions, dimensions
        r,c = startpoint[0], startpoint[1]
        dr, dc = 0, 1
        
        for _ in range(rows * cols):
            if self.nodes[(r,c)].get_typename() is 'house':
                batteries = self.sort_batteries((r,c))
                for battery in list(batteries):
                    if battery.has_space():
                        battery.add_house(self.nodes[(r,c)].get_type())
                        break
            if (r + dr < 0 or r+dr > rows or c + dc < 0 or c + dc > cols):
                dr, dc = dc, -dr
            r += dr
            c += dc
        
        print(battery.houses)
                
    def sort_batteries(self, location):
        distances = {}
        for battery in self.model.batteries:
            distance = self.model.manhattan_distance(battery.location, location)
            distances[distance] = battery
        keys = list(distances.keys())
        keys.sort()
        sorted_distances = {i: distances[i] for i in keys}
        return sorted_distances
    
    def add_house(self):

        pass