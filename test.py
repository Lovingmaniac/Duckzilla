# dit is python
from battery import Battery

batteries = []
district = 1
with open(f"data/district_{district}/district-{district}_batteries.csv") as f:
    header = f.readline()
    for line in f:
        split = line.strip().split(',')
        x = int(split[0].strip('"'))
        y = int(split[1].strip('"'))
        capacity = float(split[2])

        batteries.append(Battery(x, y, capacity))

for item in batteries:
    print(item)


        