import copy
import random
import time
import random
import math

from code.classes.model import Model
from code.visualization.visualization import visualize
from code.classes.house import House
from code.visualization.output import output

class FillBattery():
    def __init__(self, model: Model):
        self.model = model
        self.nodes = model.nodes
        self.unconnected_houses = model.unconnected_houses

    def run(self, startpoint):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.spiral_sort(startpoint)
        
        costs = self.model.calculate_costs()
        output(self.model)
        print(costs)

        # with open(f'output/histogram_fillbattery_{timestr}.txt', 'w') as f:
        #     self.spiral_sort(startpoint)
        #     costs = self.model.calculate_costs()
        #     print(costs)
        
        #     if costs < min_costs:
        #         min_costs = costs
        #         print(min_costs)
        #         # visualize(base_model)
        #     if self.model.is_solution():
        #         f.write(f'{costs}\n')
        #     else:
        #         f.write('0\n')


    def spiral_sort(self, startpoint):
        dimensions = int(math.sqrt(len(self.nodes)))
        rows, cols = dimensions, dimensions
        r,c = startpoint[0], startpoint[1]
        dr, dc = 0, 1
        grid = self.make_grid(dimensions)                        
        
        for _ in range(rows * cols):
            if self.nodes[(r,c)].get_typename() == 'house':
                batteries = self.sort_batteries((r,c))
                for battery in list(batteries.values()):
                    if battery.has_space(self.nodes[(r,c)].get_type()):
                        self.add_house(self.nodes[(r,c)].get_type(), battery)
                        print(f"battery: {battery}, {battery.houses} \n ")
                #         break
            grid[r][c] = None
            if (r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols or grid[r + dr][c + dc] is None):
                dr, dc = dc, -dr
            r += dr
            c += dc
                
    def sort_batteries(self, location):
        distances = {}
        for battery in self.model.batteries:
            distance = self.model.manhattan_distance(battery.location, location)
            distances[distance] = battery
        keys = list(distances.keys())
        keys.sort()
        sorted_distances = {i: distances[i] for i in keys}
        return sorted_distances
    
    def add_house(self, house, battery):
        battery.add_house(house)
        # self.model.make_cables()
        # index = 0
        # print(f'house: {house}, id: {id(house)}')
        # for huis in self.unconnected_houses:
        #     print(f'huis: {huis}, index: {index},  id: {id(house)}')
        #     print(huis == house)
            
        #     # if huis == house:
        #     #     new_house = self.unconnected_houses.pop(index)
        #     #     print(new_house)
            #     battery.add_house(new_house)
            #     self.model.make_cables()
            # index += 1

    def make_grid(self, dimensions):
        grid = []
        for row in range(dimensions):
            grid.append([])
            for col in range(dimensions):
                grid[row].append(col)
        
        return grid