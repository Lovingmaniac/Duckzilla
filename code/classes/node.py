from collections import namedtuple

class Node:
    def __init__(self, x, y):
        self.coordinates = namedtuple("location", "x y")(x, y)
        self.connections = []
        self.type = None
        self.typename = None
        self.is_cable = False

    def add_connection(self, node):
        self.connections.append(node)

    def get_connections(self):
        return self.connections

    def add_type(self, type):
        self.type = type
    
    def get_type(self):
        return self.type

    def set_cable(self):
        self.is_cable = True
    
    def remove_cable(self):
        self.is_cable = False

    def add_typename(self, typename):
        self.typename = typename
    
    def get_typename(self):
        return self.typename
    def __repr__(self):
        return f"location: {self.coordinates}"
