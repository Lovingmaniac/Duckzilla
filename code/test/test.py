from collections import namedtuple

loc = namedtuple("Location", "x y")(1, 2)
print(loc.x)