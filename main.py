from code.classes.grid import Grid
from code.visualization.visualization import visualize

if __name__ == "__main__":
    grid = Grid()

    grid.make_nodes()
    grid.add_connections()
    grid.load_grid(1)
    visualize(grid)

    for item in grid.houses:
        print(item)

    for item in grid.batteries:
        print(item)

