import copy
import time
import random

from code.classes.model import Model
from code.visualization.visualization import visualize
from code.classes.node import Node
from code.classes.battery import Battery
from code.visualization.output import output

class BreadthFirst():
    """
    A Breadth First algorithm that makes a queue for every state in which the cables can be laid for every house.
    """
    def __init__(self, input_model: Model):
        self.model: Model = input_model
        self.nodes: Node = input_model.nodes

        self.states: list = []

        self.best_value = 100000
        self.best_solution = None
        
        self.visited_state_count: int = 0
        self.max_states_size: int = len(self.states)
        self.states_sizes: list = []
        self.solution_count = 0

    def get_next_state(self) -> list:
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)

    def build_children(self, node: Node, list_cables: list) -> None:
        """
        Creates all possible child states and adds them to the list.
        """

        # finds all the connections that are possible
        values = node.get_connections()
        
        # iterates over the values for the connections
        for value in values:

            # copies the list of cables and appends the new state
            new_list_cables = copy.deepcopy(list_cables)
            new_list_cables.append(self.nodes[value])

            # when the value is the archive the new value is added
            if not value in self.archive:
                self.archive.add(value)
                self.states.append(new_list_cables)
    
    def check_solution(self, new_model: Model) -> None:
        """
        Checks and accepts better solutions than the current solution.
        """ 
        # calculates the costs of the model
        new_value = new_model.calculate_costs()

        # saves the best solution
        if new_value <= self.best_value:
            self.best_solution = new_model
            self.best_value = new_value

    def size(self) -> int:
        # returns the size of the list of states
        return len(self.states)

    def done(self) -> bool:
        return self.size() == 0
    
    def run(self) -> None:
        """
        runs the breadthfirst algorithm.
        """
        # initialize a count variable to keep track of the number of houses processed
        count = 0
        
        # iterates over the batteries in the model
        for battery in self.model.batteries:
            # define the end node as current location battery
            end_node = set([self.nodes[(battery.location.x, battery.location.y)]])
            # shuffles the list of houses connected to this battery
            houses = self.sort_houses(battery)
            # random.shuffle(houses)

            # iterate over the houses connected to this battery
            for house in houses:
                house[0].cables = []
                
                count += 1
                print(house, count)
                
                # define the start node as the location of this house
                start_node = self.nodes[(house[0].location.x, house[0].location.y)]

                # initialize the state and archive for the algorithm    
                self.states = [[start_node]]
                self.archive = set()

                # keep searching for a path from start to end node until it has been found
                while not self.done():
                    # get the next state
                    new_state = self.get_next_state()

                    #statistical analysis
                    self.visited_state_count += 1
                    self.max_states_size = max(self.size(), self.max_states_size)
                    self.states_sizes.append(self.size())

                    # get the last node in the current state
                    last_node = new_state[-1]

                    # if the last node is not the end node set, build children
                    if last_node not in end_node:
                        self.build_children(last_node, new_state)
                    
                    # if the last node is the end node, add the cables to the house and the end node set
                    # break out of the loop
                    else:
                        for cable in new_state:
                            house[0].add_cable(cable.coordinates)
                            end_node.add(self.nodes[cable.coordinates])
                            self.nodes[cable.coordinates].set_cable()
                        break
        
        # visualize the final model and generate a output file.
        visualize(self.model)
        output(self.model)
        self.file_output(self.model)
    

    def sort_houses(self, battery: Battery):
        """
        sort the houses on the distance between it and the battery, stores it in a dictionary
        """
        distances = {}
        
        # iterates over the houses and calculates the distance
        for house in battery.houses:
            distance = self.model.manhattan_distance(battery.location, house.location)
            distances[house] = distance
        
        # sorts the houses and returns them
        sorted_houses = sorted(distances.items(), key=lambda x:x[1], reverse= True)
        return sorted_houses

    def file_output(self, model: Model)-> None:
        """
        takes a model and appends the data to a file
        """
        # makes a timestring
        timestr = time.strftime("%Y%m%d-%H%M%S")

        # open the file and append the data
        with open(f'output/output_breadthfirst.txt', 'a') as f:
            if model.is_solution():
                f.write(f'dag/tijd: {timestr}\nvisited states: {self.visited_state_count}\n max state size: {self.max_states_size} \n costs: {model.calculate_costs()}\n\n')
            else:
                f.write('Not a valid solution\n')