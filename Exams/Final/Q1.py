class Vehicle:
    def __init__(self, VIN_NUM, list_location, speed):

        self.VIN_NUMBER = VIN_NUM
        self.list_location = list_location
        self.vehicle_speed = speed



class Motorcycle(Vehicle):
    
    def __init__(self,VIN_NUM, list_location, speed,cylinder_no,wheel_no,registration_status):
        super().__init__(VIN_NUM, list_location, speed)

        

        
        self.cylinder_no = cylinder_no
        self.wheel_no = wheel_no
        self.registration_status = registration_status

    
    def update_location(self,longitude,latitude):
        self.list_location = [longitude,latitude]

    def change_speed(self,new_speed):
        self.vehicle_speed = new_speed

class Car(Vehicle):
    def __init__(self,VIN_NUM, list_location, speed,passenger_no, registration_status):
        super().__init__(VIN_NUM, list_location, speed)

        self.passenger_no = passenger_no
        self.registration_status = registration_status
    
    def add_passenger(self, add_amount):
        self.passenger_no += add_amount

    def reduce_passenger(self,reduce_amount):
        self.passenger_no -= reduce_amount

    def update_location(self,longitude,latitude):
        self.list_location = [longitude,latitude]

    def change_speed(self,new_speed):
        self.vehicle_speed = new_speed


class MVA:
    def __init__(self,vehicles_processed,mva_location) -> None:
        self.vehicles_processed = vehicles_processed
        self.mva_location = mva_location
        
    def update_registration_status(self,vehicle):
        print(f"Current registration status of vehicle {vehicle.VIN_NUMBER} is: {vehicle.registration_status}")
        change_request = input("Change T/F?")
        if change_request == "T":
            vehicle.registration_status = True
            self.increment_processed_vehicles()
        elif change_request == "F":
            vehicle.registration_status = False
            self.increment_processed_vehicles()
        else:
            print("Error.")
        

        print(f"Total processed vehicles of this location in {self.mva_location}:{self.vehicles_processed}")

    def increment_processed_vehicles(self):
        self.vehicles_processed +=1


captechMVA = MVA(vehicles_processed=0,mva_location="somewhere in maryland")

newcar1 = Car(VIN_NUM="824JK",list_location=[28,15],speed="15mph",passenger_no=2,registration_status=False)

print(newcar1.passenger_no)
newcar1.add_passenger(2)
print(newcar1.passenger_no)

print(f"newcar current registration status: {newcar1.registration_status}")

captechMVA.update_registration_status(newcar1)

print(f"newcar current registration status: {newcar1.registration_status}")