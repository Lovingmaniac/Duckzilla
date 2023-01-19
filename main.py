from code.classes.model import Model
from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output

if __name__ == "__main__":
    # create new grid and model from data
    grid = Grid()
    grid.make_nodes()
    grid.load_grid(1)

    model = Model(grid)
    
    #----------------random assignment of houses to batteries---------------
    rand.baseline(model, 100000)

    # rand.run(model)
    # output(new_model)
    # visualize(model)

    #---------------next algorithm--------------------
