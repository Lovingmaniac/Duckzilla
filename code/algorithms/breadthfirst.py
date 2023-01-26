import copy
import time
import random
import math

from code.classes.model import Model
from code.visualization.visualization import visualize
from code.classes.house import House
from code.classes.node import Node
from code.visualization.output import output
from code.algorithms.greedy_battery import FillBattery

class BreadthFirst():

    def __init__(self, input_model: Model):
        self.model = input_model
        self.nodes = input_model.nodes
        self.unconnected_houses = input_model.unconnected_houses

        self.states = []

        self.best_value = 100000
        self.best_solution = None
        
        self.visited_state_count = 0
        self.max_states_size = len(self.states)
        self.states_sizes = []
        self.solution_count = 0

    def get_next_state(self) -> list:
        return self.states.pop(0)

    def build_children(self, node: Node, list_cables):
        values = node.get_connections()
        # print(values)
        
        for value in values:
            new_list_cables = copy.deepcopy(list_cables)
            new_list_cables.append(self.nodes[value])
            if not value in self.archive:
                self.archive.add(value)
                self.states.append(new_list_cables)
    
    def check_solution(self, new_model: Model):
            new_value = new_model.calculate_costs()

            if new_value <= self.best_value:
                self.best_solution = new_model
                self.best_value = new_value

    def size(self):
        return len(self.states)

    def done(self):
        return self.size() == 0
    
    def run(self):
        # connect houses to batteries
        fb = FillBattery(self.model)
        fb.spiral_sort((0,0))

        count = 0
        for battery in self.model.batteries:
            end_node = set([self.nodes[(battery.location.x, battery.location.y)]])
            random.shuffle(battery.houses)
            for house in battery.houses:
                count += 1
                print(house, count)
                start_node = self.nodes[(house.location.x, house.location.y)]
                    
                self.states = [[start_node]]
                self.archive = set()
            
                while not self.size() == 0:
                    new_state = self.get_next_state()

                    #statistical analysis
                    self.visited_state_count += 1
                    self.max_states_size = max(self.size(), self.max_states_size)
                    self.states_sizes.append(self.size())

                    last_node = new_state[-1]
                    if last_node not in end_node:
                        self.build_children(last_node, new_state)
                    else:
                        for cable in new_state:
                            house.add_cable(cable.coordinates)
                            end_node.add(self.nodes[cable.coordinates])
                        break

        visualize(self.model)
        # breakpoint()
        
        # print(self.check_solution(self.model))

                    

                    
            


            
            




    







# def make_cables_random(self, dim):
#         for battery in self.model.batteries:
#             for house in battery.houses:
#                 x_house, y_house = house.location
#                 x_battery, y_battery = battery.location
                
#                 house.add_cable((x_house, y_house))
#                 self.nodes[(x_house, y_house)].set_cable()

#                 x_step = 1
#                 y_step = 1

#                 directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
#                 random.shuffle(directions)

#                 dir = directions.pop()
#                 if x_house + dir[0] >= 0 or x_house + dir[0] < dim or y_house + dir[1] >= 0 or y_house + dir[1] < dim:
#                     pass
