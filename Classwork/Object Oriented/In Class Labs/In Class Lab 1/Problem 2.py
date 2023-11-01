#create a hierarchy of animals
#create a speak() method to make the animal speak

#base class is animal
#derived classes are dog and cat

class Animal:
    def __init__(self, animal_sound):
        self.animal_sound = animal_sound

    def speak(self):
        print(self.animal_sound)

class Dog(Animal):
    def __init__(self, animal_sound) -> None:
        self.animal_sound = "woof"
        super().__init__(animal_sound)
    

class Cat(Animal):
    def __init__(self, animal_sound) -> None:
        self.animal_sound = "meown"
        super().__init__(animal_sound)


base_animal = Animal.speak()
print(base_animal)