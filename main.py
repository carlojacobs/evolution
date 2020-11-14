# Evolution Simulator

from map import Map
from block import Block
from entity import Entity
import vars
import random

global map

def random_int(min, max):
    return random.randint(min, max)

def main():
    map_size = vars.map_size
    grass = Block("grass", False)
    # Generate initial map
    initial_conditions = []
    for i in range(map_size):
        new_row = []
        for j in range(map_size):
            grass.food = bool(random.getrandbits(1))
            new_row.append(grass)
        initial_conditions.append(new_row)
    # Generate initial entities
    entities = []
    for i in range(50):
        energy = 1000
        speed = random_int(500,1000)
        hunger = 0
        thirst = 0
        age = random_int(1,15)
        vision_radius = random_int(0,map_size/2)
        position = [random_int(0, map_size-1), random_int(0, map_size-1)]
        gender_options = ["male", "female"]
        random_gender_options_index = random_int(0,1)
        gender = gender_options[random_gender_options_index]
        new_entity = Entity(energy, speed, age, hunger, thirst, vision_radius, position, gender)
        entities.append(new_entity)

    map = Map(map_size, initial_conditions, entities)
    map.info()
    map.entities[0].move([0,1])

if __name__ == "__main__":
    main()
