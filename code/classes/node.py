class Node():
    def __init__(self, x, y, uid):
        self.coordinates = (x, y)
        self.connections = {}
        self.id = uid

    def add_connection(self, node):
            self.connections[node.id] = node
    
    
