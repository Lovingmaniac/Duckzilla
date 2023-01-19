class Node:
    def __init__(self, x, y):
        self.coordinates = (x, y)
        self.connections = []
        self.type = None
        self.is_cable = False

    def add_connection(self, node):
        self.connections.append(node)

    def add_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_cable(self):
        self.is_cable = True
    
    def remove_cable(self):
        self.is_cable = False


    def __repr__(self):
        return f"id: {self.id}, location: {self.coordinates}"
