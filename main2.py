from code.classes.model import Model
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output

if __name__ == "__main__":
    model = Model()

    model.make_nodes()
    model.add_connections()
    model.load_grid(3)
    

    new_grid = rand.make_new_grid(model)
    # print(rand.baseline(new_grid))
    rand.run(new_grid)
    # rand.baseline(new_grid, 1)
    print(f'score: {rand.get_score(new_grid)}')

    output(new_grid)
    # visualize(new_grid)
