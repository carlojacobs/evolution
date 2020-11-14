# Map
import matplotlib.pyplot as plt

class Map():
    def __init__(self, size, initial_conditions, entities):
        self.size = size
        # Array of dimension size*size with elements of type Block
        self.initial_conditions = initial_conditions
        self.entities = entities
        self.carry_map()

    def carry_map(self):
        for entity in self.entities:
            entity.update_map_conditions(self.initial_conditions)

    def info(self):
        print(f"Size: {self.size}\nInitial conditions: {len(self.initial_conditions)}\nNum of Entities: {len(self.entities)}")
