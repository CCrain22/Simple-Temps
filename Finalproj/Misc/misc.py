import sys 
class Dog:
    def __init__(self, name):
        self.name = name
        self.sound = None
    def speak(self, sound):
        self.sound = sound
    def printdog(self):
        print(self.name, self.sound)

class Golden_R(Dog):
    def speak(self, sound):
        self.sound = 'woof'
    
dog_1 = Dog('linden')
dog_1.speak('arf')
dog_1.printdog()

Golden_R_1 = Golden_R('Ron')
Golden_R_1.speak('arf')
Golden_R_1.printdog()

#use self to refer to instance

# class Car:
#     def __init__(self, color, speed, year_of_model):
#         self.color = color 
#         self.speed = speed
#         self.year_of_model = year_of_model
#     def printcar(self):
#         print(self.color, self.speed, self.year_of_model)

# Toyota_0 = Car('sage green', 'medium', '2015')
# Toyota_0.printcar()

# Nissan_0 = Car('grey', 'medium', '1990?')
# Nissan_0.printcar()
