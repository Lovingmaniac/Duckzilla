import math

from code.classes.model import Model
from code.classes.house import House

class FillBattery():
    def __init__(self, model: Model):
        self.model = model
        self.nodes = model.nodes
        self.unconnected_houses = model.unconnected_houses

    def run(self, startpoint: tuple):
        """
        runs the code with a startpoint
        """
        self.spiral_sort(startpoint)
        self.model.make_cables()
        costs = self.model.calculate_costs()

    def spiral_sort(self, startpoint: tuple):
        """
        goes through a grid in a spiral from the outside to the middle, and connects houses and batteries.
        """
        
        #calculates the dimensions of the grid and sets the number of rows and columns
        dimensions = int(math.sqrt(len(self.nodes)))
        rows, cols = dimensions, dimensions
        r,c = startpoint[0], startpoint[1]
        dr, dc = 0, 1

        # set up the grid
        grid = self.make_grid(dimensions)

        # set up an archive
        archive = set()

        # go through the grid
        for _ in range(rows * cols):
            
            #searches the grid voor nodes that are houses, and checks if it has been passed. 
            if self.nodes[(r,c)].get_typename() == 'house' and self.nodes[(r,c)] not in archive:
                
                # sorts batteries on distance from the house
                batteries = self.sort_batteries((r,c))
                # indexes the house to take the right one out of the list
                index = self.get_index_house((r,c))
                # take the house out of the list
                house = self.unconnected_houses.pop(index)

                # goes over the sorted batteries and adds the house if it has space
                for battery in list(batteries.values()):
                    if battery.has_space(house):
                        battery.add_house(house)
                        house.set_connected()
                        break
            
            # adds the visited node to the archive
            archive.add(self.nodes[(r,c)])

            # sets the grid to none, so it will not be visited again
            grid[r][c] = None
            
            # sets the borders of the grid
            if (r + dr < 0 or r + dr > rows - 1 or c + dc < 0 or c + dc > cols - 1 or grid[r + dr][c + dc] is None):
                dr, dc = dc, -dr
            
            # moves through the grid
            r += dr
            c += dc

    def sort_batteries(self, location):
        """
        function to sort the batteries on distance to the house
        """
        # initialises a distances dictionary with the distance as key
        distances = {}

        # calculates the distance for every battery
        for battery in self.model.batteries:
            distance = self.model.manhattan_distance(battery.location, location)
            distances[distance] = battery
        
        # makes a list of the dictionary keys, and sorts it, then sorts the dictionary
        keys = list(distances.keys())
        keys.sort()
        sorted_distances = {i: distances[i] for i in keys}
        return sorted_distances

    def make_grid(self, dimensions):
        """
        makes a grid with --dimensions rows and columns
        """
        grid = []
        for row in range(dimensions):
            grid.append([])
            for col in range(dimensions):
                grid[row].append(col)
        
        return grid

    def get_index_house(self, location):
        """
        Takes the location of a house and returns the index of it in unconnected_houses
        """
        index = 0
        for house in self.unconnected_houses:
            if house.location.x == location[0] and house.location.y == location[1]:
                return index
            index += 1
