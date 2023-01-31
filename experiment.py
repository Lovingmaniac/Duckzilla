import subprocess
import time

from code.algorithms.hillclimber import Hillclimber
from code.classes.model import Model
from code.classes.grid import Grid
from code.visualization.visualization import visualize
from code.algorithms import randomise as rand
from code.visualization.output import output
from code.algorithms.greedy_battery import FillBattery as fb
from code.classes.node import Node
from code.algorithms.breadthfirst import BreadthFirst
from code.algorithms.iteration import Iteration
from code.algorithms import greedy_iteration_bf

start = time.time()
n_runs = 0

while time.time() - start < 3600:
    print(f"run: {n_runs}")
<<<<<<< HEAD
    subprocess.call(["timeout", "1000", "python3", "code/algorithms/greedy_iteration_algorithm.py"])
    n_runs += 1
=======
    subprocess.call(["timeout", "60", "python3", "main.py"])
    n_runs += 1

"""
Alle algoritmes worden 2 uur gerund:

Deze worden:

random - 90 graden
random - best first
random - breadthfirst

Greedy - 90 graden
Greedy - best first
Greedy - breadth first

Iteration - 90 graden
Iteration - best first
Iteration - breadthfirst

Hillclimber - 90 graden
Hillclimber - best first
Hillclimber - breadthfirst

"""
>>>>>>> 270f5111cb1f74569662d566de786c536e143504
