from house import House
from battery import Battery
from grid import Grid

if __name__ == "__main__":
    grid = Grid()
    grid.batteries.append(Battery(38, 12, 1507.0))
    grid.houses.append(House(33, 7, 39.46))
    grid.houses.append(House(30, 12, 66.05))
