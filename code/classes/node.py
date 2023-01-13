class Node():

    def __init__(self, x, y, uid):
        self.coordinates = (x, y)
        self.connections = []
        self.type = None

    def add_connection(self, node):
        self.connections.append(node)

    def add_type(self, type):
        self.type = type
