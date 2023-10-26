class Cars:
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles'
    
blue_car = Cars(color= "blue", mileage= 20000)
red_car = Cars(color= "red", mileage= 30000)

for car in (blue_car,red_car):
    print (car)