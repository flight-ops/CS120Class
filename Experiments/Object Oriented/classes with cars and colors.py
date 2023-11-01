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


print("\nNow driving blue car for 5000 miles\n")
new_mileage = blue_car.mileage + 5000

blue_car.mileage = new_mileage

for car in (blue_car,red_car):
    print (car)