from code.classes import grid, battery, house


if __name__ == "__main__":
    grid = Grid()
    grid.load_grid(1)
    grid.make_grid()

    for item in grid.houses:
        print(item)

    for item in grid.batteries:
        print(item)

