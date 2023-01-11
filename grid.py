from battery import Battery
from house import House

class Grid:
  
  def __init__(self) -> None:
      self.houses
      self.batteries
  
  def load_grid(self, district):
      # load battery data
      with open(f"data/district_{district}/district-{district}_batteries.csv") as f:
          header = f.readline()
          for line in f:
              split = line.strip().split(',')
              x = int(split[0].strip('"'))
              y = int(split[1].strip('"'))
              capacity = float(split[2])
  
              self.batteries.append(Battery(x, y, capacity))

      with open(f"data/district_{district}/district-{district}_houses.csv") as f:
          header = f.readline()
          for line in f:
              split = line.strip().split(',')
              x = int(split[0])
              y = int(split[1])
              capacity = float(split[2])
  
              self.houses.append(House(x, y, capacity))

          

  