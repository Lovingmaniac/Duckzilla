class House:
    def __innit__(self, x: int, y: int, output: float) -> None:
        self.location = {x, y}
        self.output = output
        self.cables = [tuple]

    def add_cable(self, location: tuple) -> None:
        '''adds a cable to the house object'''
        self.cables.append(location)

    def remove_cable(self, location: tuple) -> None:
        '''removes cable from house object if it is there'''
        if location not in self.cables:
            return 1
        
        self.cables.remove(location)

    def get_output(self) -> float:
        '''returns the output of a house object'''
        return self.output