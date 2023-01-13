from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomize as rand

if __name__ == "__main__":
    grid = Grid()

    grid.make_nodes()
    grid.add_connections()
    grid.load_grid(1)

    random_grid = rand.Randomize(grid)
    random_grid.run()

    print(len(random_grid.grid.houses))