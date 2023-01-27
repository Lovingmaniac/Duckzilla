import copy
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
        self.model.make_cables()
        costs = self.model.calculate_costs()
        # output(self.model)
        # visualize(self.model)
        # print(costs)
        # print(self.model.is_solution())

        # with open(f'output/histogram_fillbattery_{timestr}.txt', 'w') as f:
        #     self.spiral_sort(startpoint)
        #     self.model.make_cables()
        #     costs = self.model.calculate_costs()
        #     # print(costs)
        #     output(self.model)
        #     min_costs = 100000
        #     if costs < min_costs:
        #         min_costs = costs
        #         # print(min_costs)
        #         # visualize(self.model)
        #     if self.model.is_solution():
        #         f.write(f'{costs}\n')
        #     else:
        #         f.write('NaN\n')


    def spiral_sort(self, startpoint):
        dimensions = int(math.sqrt(len(self.nodes)))
        rows, cols = dimensions, dimensions
        r,c = startpoint[0], startpoint[1]
        dr, dc = 0, 1
        grid = self.make_grid(dimensions)
        archive = set()                        
        
        for _ in range(rows * cols):
            if self.nodes[(r,c)].get_typename() == 'house' and self.nodes[(r,c)] not in archive:
                batteries = self.sort_batteries((r,c))
                index = self.get_index_house((r,c))
                house = self.unconnected_houses.pop(index)
                for battery in list(batteries.values()):
                    if battery.has_space(house):
                        battery.add_house(house)
                        house.set_connected()
                        break
            archive.add(self.nodes[(r,c)])
            grid[r][c] = None
            if (r + dr < 0 or r + dr > rows - 1 or c + dc < 0 or c + dc > cols - 1 or grid[r + dr][c + dc] is None):
                dr, dc = dc, -dr
            r += dr
            c += dc
        # print(self.unconnected_houses)
                
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
        pass
        # self.model.make_cables()
        # index = 0
        # # print(f'house: {house}, id: {id(house)}')
        # for huis in self.unconnected_houses:
        #     # print(f'huis: {huis}, index: {index},  id: {id(house)}')
        #     # print(huis == house)
            
        #     if huis == house:
        #         new_house = self.unconnected_houses.pop(index)
        #         print(new_house)
        #         battery.add_house(new_house)
        #         self.model.make_cables()
        #     index += 1

    def make_grid(self, dimensions):
        grid = []
        for row in range(dimensions):
            grid.append([])
            for col in range(dimensions):
                grid[row].append(col)
        
        return grid

    def get_index_house(self, location):
        index = 0
        for house in self.unconnected_houses:
            if house.location.x == location[0] and house.location.y == location[1]:
                return index
            index += 1
    
    