class Pet:
    def __init__(self, name, tricks, pet_type):
        self.name = name
        self.tricks = tricks
        self.energy = 50
        self.health = 50
        self.pet_type=pet_type
        self.pet_noise = "woof"
# sleep() - increases the pets energy by 25
    def sleep(self):
        if self.energy < 76:
            self.energy += 25
            print (f"{self.name} has {self.energy} energy.")
        else:
            self.energy = 100
            print (f"{self.name} is fully rested.")
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        if self.energy < 96:
            self.energy += 5
            print (f"{self.name} has {self.energy} energy.")
        else:
            self.energy = 100
        if self.health < 91:
            self.health += 10
            print (f"{self.name} has {self.health} health.")
        else:
            self.health = 100
            print (f"{self.name} is full.")
# play() - increases the pet's health by 5
    def play(self):
        if self.health < 96:
            self.health += 5
            print (f"{self.name} has {self.health} health.")
        else:
            self.health = 100;
            print (f"{self.name} is in perfect health.")
# noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} says: {self.pet_noise}!")

class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks, "dog")
        self.pet_noise = "woof"

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks, "cat")
        self.pet_noise = "meow"


