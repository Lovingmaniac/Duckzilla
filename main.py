from code.classes.grid import Grid


if __name__ == "__main__":
    grid = Grid()
    grid.make_nodes()
    grid.add_connections()
    grid.load_grid(1)

    for item in grid.houses:
        print(item)

    for item in grid.batteries:
        print(item)
