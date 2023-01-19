import random
import copy
from code.classes.model import Model
from code.classes.house import House


def get_ordered_list(houses:list[House], x: int, y: int) -> list[tuple]:
    """ 
    Takes a list of houses and x and y coordinates of a single point
    and returns a list of tuples based on the distance to
    the single point in descending order
    pre:    houses is a list of houses
    post:   returns a list of houses
    """
    houses.sort(key = lambda h: (h.location[0] - x)**2 + (h.location[1] - y)**2, reverse= True)
    return houses

def run(model: Model):

    
    # randomise the order of the batteries
    random.shuffle(model.batteries)

    for battery in model.batteries:
        # model.unconnected_houses = get_ordered_list(model.unconnected_houses, battery.location[0],
        #                           battery.location[1])
        house = model.unconnected_houses.pop()
        
        while battery.has_space(house) and model.unconnected_houses:
            # battery.add_house(house)
            house = model.unconnected_houses.pop()
    model.make_cables()
    

