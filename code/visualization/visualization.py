import matplotlib.pyplot as plt
import json
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import time

# Read image
# image = imread('house.png')
timestr = time.strftime("%Y%m%d-%H%M%S")

def visualize(model):
    battery_img = "data/battery.jpg"
    house_img = "data/house2.jpg"

    # -------------------------------------test data----------------------------
    # dictionary = json.load(open(f'{output_file}.json', 'r'))
    # district_info = dictionary.pop(0)
    # x_batteries = []
    # y_batteries = []
    # print(dictionary)
    # for battery in dictionary:
    #     location = battery['location'].split(',')
    #     x_batteries.append(int(location[0]))
    #     y_batteries.append(int(location[1]))

    # -------------------------------------source data from grid----------------
    x_batteries = []
    y_batteries = []
    x_houses = []
    y_houses = []

    # go over each battery and house node in grid
    for battery in model.batteries:
        x_batteries.append(battery.location[0])
        y_batteries.append(battery.location[1])

    for house in model.houses:
        x_houses.append(house.location[0])
        y_houses.append(house.location[1])

    # -------------------------------------plot---------------------------------
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    imscatter(x_batteries, y_batteries, battery_img, zoom=0.08, ax=ax)
    imscatter(x_houses, y_houses, house_img, zoom=0.08, ax=ax)
    for battery in model.batteries:
        colors = ["red", "blue", "green", "yellow", "orange"]
        for house in battery.houses:
            x_cable = []
            y_cable = []
            for cable in house.cables:
                x_cable.append(cable[0])
                y_cable.append(cable[1])
                ax.plot(x_cable, y_cable, color=colors[battery.id - 1])
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_xticks(range(0, 55, 10))
    ax.set_yticks(range(0, 55, 10))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.grid(True, which="both", axis="both", linestyle="-", color="gray", linewidth=0.5)
    fig.suptitle(f'costs: {model.calculate_costs()}')
    plt.savefig(f"output/grid_{timestr}.png")
    plt.show()


def imscatter(x, y, image, ax=None, zoom=1):
    if ax is None:
        ax = plt.gca()
    try:
        image = plt.imread(image)
    except TypeError:
        # Likely already an array...
        pass
    im = OffsetImage(image, zoom=zoom)
    x, y = np.atleast_1d(x, y)
    artists = []
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(im, (x0, y0), xycoords="data", frameon=False)
        artists.append(ax.add_artist(ab))
    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists


if __name__ == "__main__":
    visualize("example_output")
