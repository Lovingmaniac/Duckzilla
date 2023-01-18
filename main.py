from code.classes.model import Model
from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output

if __name__ == "__main__":
    grid = Grid()
    grid.make_nodes()
    grid.load_grid(1)
    
    
    model = Model(grid)
    
    new_model = model.copy()
    # print(rand.baseline(new_grid))
    
    rand.baseline(new_model, 10)
    print(f'score: {rand.get_score(new_model)}')
    
    # rand.run(new_model)
    # output(new_model)
    # visualize(new_grid)
