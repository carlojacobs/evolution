# Entity
import vars

class Entity():
    def __init__(self, energy, speed, age, hunger, thirst, vision_radius, position, gender):
        self.energy = energy
        self.speed = speed
        self.hunger = hunger
        self.thirst = thirst
        self.age = age
        self.vision_radius = vision_radius
        self.position = position
        self.gender = gender
        self.map_conditions = []

    def update_map_conditions(self, new_map_conditions):
        self.map_conditions = new_map_conditions

    def eat(self, block):
        energy_difference = 1
        hunger_difference = -1
        self.energy += energy_difference
        self.hunger += hunger_difference
        block.food = False

    def drink(self):
        thirst_difference = -1
        self.thirst += thirst_difference

    def get_block(self):
        position = self.position
        print("Position: ", position)
        block = self.map_conditions[position[1]][position[0]]
        return block

    def food_available(self):
        block = self.get_block()
        if block.food:
            return True
        else:
            return False

    def water_available(self):
        block = self.get_block()
        if block.type == "water":
            return True
        else:
            return False

    def move(self, position_difference):
        position = self.position
        new_position = [position[0]+position_difference[0], position[1]+position_difference[1]]
        new_x = new_position[0]
        new_y = new_position[1]
        if (new_x >= 0 and new_x <= vars.map_size) and (new_y >= 0 and new_y <= vars.map_size):
            self.position = new_position

        # Check if it can eat or drink and do so
        if self.food_available():
            self.eat(self.get_block())
        if self.water_available():
            self.drink()
