class Vehicle():
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

        #show details of the model
    def display_info(self):
        print(f'Make: {self.manufacturer} \nModel:{self.model}')

class Car(Vehicle):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model)
        self.year = year

    def display_info(self):
        print(f'Make: {self.manufacturer} \nModel:{self.model}\nYear: {self.year}' )

class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)




generic_vehicle = Vehicle(manufacturer= "Toyota", model= "Prius")

specific_vehicle = Car(year="2023", manufacturer="Toyota", model= "Prius Prime")



generic_vehicle.display_info()

specific_vehicle.display_info()