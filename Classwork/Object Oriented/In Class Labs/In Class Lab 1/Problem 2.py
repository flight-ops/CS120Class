#create a hierarchy of animals
#create a speak() method to make the animal speak

#base class is animal
#derived classes are dog and cat

class Animal:
    def __init__(self):
        self.animal_sound = "huh"

    def speak(self):
        print(self.animal_sound)
        

class Dog(Animal):
    def __init__(self):
        self.animal_sound = "woof"

    def speak(self):
        print(self.animal_sound)

class Cat(Animal):
    def __init__(self):
        self.animal_sound = "meow"

    def speak(self):
        print(self.animal_sound)


base_animal = Animal()

dog_object = Dog()

dog_object.speak()