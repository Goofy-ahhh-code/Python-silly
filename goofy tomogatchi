class Tamagotchi: 
    def __init__(self, name, breed):# -*- coding: latin-1 -*-
        self.name = name
        self.breed = breed
        self.happylevel = 1
    
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")
    
    def pet(self):
        self.happylevel = self.happylevel + 1
        print(f"{self.name} is happy")
        print(f"happiness level = {self.happylevel}")
    
    def feed(self):
        self.happylevel = self.happylevel + 2
        print(f"{self.name} was fed and is happy")
        print(f"happiness level = {self.happylevel}")
        
        
uinput = input("name your Tamagotchi: ")
uinput2 = input("what breed is your Tamagotchi: ")
my_dog = Tamagotchi(uinput, uinput2)
opt = "1"
my_dog.bark() 

while opt != "3":
    opt = input("interact, 1 = pet, 2 = feed, 3 = quit: ")
    if opt == "1":
        my_dog.pet()
    if opt == "2":
        my_dog.feed()
