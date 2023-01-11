from house import House


class Battery:

  def __init__(self, x: int, y: int, capacity: float):
      self.location = (x, y)
      self.capacity = capacity
      self.current_capacity = capacity
      self.houses: list[House] = []

  def __repr__(self):
    return f'loc:{self.location}, cap:{self.current_capacity}'

  def add_house(self, house: House) -> None:
      """ Adds a house to self and updates current capacity"""
      self.houses.append(house)
      self.current_capacity -= house.get_output()

  def remove_house(self, house: House) -> None:
      """ Removes a house from self and updates current capacity"""
      self.houses.delete(house)
      self.current_capacity += house.getoutput()

  def get_capacity(self) -> float:
      return self.current_capacity

  def get_location(self):
      return f'{self.location[0]},{self.location[1]}'

  def has_space(self, house: House) -> bool:
      """ 
          Returns true if the battery has sufficient space for a house
          else returns false.
      """
      if house.get_output() > self.current_capacity:
          return False
      else:
          return True

    

