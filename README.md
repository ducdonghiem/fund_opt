# Harvest Problem

This repository contains solutions to the Harvest Problem, which involves optimizing the harvesting schedule for a set of agricultural fields to comply with both minimum and maximum processing capacity constraints at a processing plant, while minimizing the difference in the number of agricultural products harvested between days. 

Annotation: There are N fields, each field i has a yield of d(i) and must be harvested between day s(i) and e(i).

This is an academic project regarding the course Fundamentals of Optimization of Hanoi University of Science and Technology. For more details, please consult the `report optimiztion.pdf` file.

## Files

- `data.txt`: A sample data folder with different sizes for the problem.

- `harvest_backtracking.py`: A solution to the Harvest Problem using backtracking.

- `harvest_SimulatedAnnealing.py`: A solution to the Harvest Problem using simulated annealing.

- `harvest_genetic.py`: A solution to the Harvest Problem using genetic algorithm.

- `harvest_CSP.py`: A solution to the Harvest Problem using constraint programming.

- `harvest_MIP.py`: A solution to the Harvest Problem using integer linear programming.

- `read_data.py`:  Reads the data text file and returns N, m, M, d, s, e and n.

## Usage

In order to use the `read_data.py` to read the data file correctly, please make sure to adjust the file path according to your environment. 