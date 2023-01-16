from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output

if __name__ == "__main__":
    grid = Grid()

    grid.make_nodes()
    grid.add_connections()
    grid.load_grid(1)
    visualize(grid)

    new_grid = rand.make_new_grid(grid)
    rand.run(new_grid)
    print(rand.get_score(new_grid))
    output(new_grid)
