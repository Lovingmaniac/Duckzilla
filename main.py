from code.classes.grid import Grid
from code.visualization.visualization import visualize

if __name__ == "__main__":
    grid = Grid()
    grid.load_grid(1)
    visualize(grid)
