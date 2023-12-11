class Vehicle:
    def __init__(self, VIN_NUM, list_location, color, speed, cylinder_no, wheel_no, passenger_no, registration_status):

        self.VIN_NUMBER = VIN_NUM
        self.list_location = list_location
        self.color = color
        self.vehicle_speed = speed

        self.cylinder_no = cylinder_no
        self.wheel_no = wheel_no
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
        #print current vehicle VIN and status
        print(f"Current registration status of vehicle {vehicle.VIN_NUMBER} is: {vehicle.registration_status}")

        #prompt user for a change
        #increment processed vehicle count by 1, then print the new registration status
        change_request = input("Change registration status, T/F\n")
        if change_request == "T":
            vehicle.registration_status = True
            self.increment_processed_vehicles()
            print(f"Changed registration status of vehicle {vehicle.VIN_NUMBER} to: {vehicle.registration_status}")
        elif change_request == "F":
            vehicle.registration_status = False
            self.increment_processed_vehicles()
            print(f"Changed registration status of vehicle {vehicle.VIN_NUMBER} to: {vehicle.registration_status}")
        else:
            print("Error.")
        

        print(f"Total processed vehicles of this location in {self.mva_location}:{self.vehicles_processed}\n")

    def increment_processed_vehicles(self):
        self.vehicles_processed +=1



def main():
    captechMVA = MVA(vehicles_processed=0,mva_location="somewhere in maryland")

    newcar1 = Vehicle(VIN_NUM="824JK",list_location=[28,15],speed="15mph",color="pastel blue",cylinder_no=4,wheel_no=4,passenger_no=2,registration_status=False)
    newcar2 = Vehicle(VIN_NUM="NMPD42",list_location=[28,15],speed="15mph",color="gray",cylinder_no=4,wheel_no=4,passenger_no=4,registration_status=False)
    newcar3 = Vehicle(VIN_NUM="MC117",list_location=[28,15],speed="50mph",color="warthog green",cylinder_no=4,wheel_no=4,passenger_no=2,registration_status=False)
    newbike1 = Vehicle(VIN_NUM="76NM",list_location=[14,94],speed="30mph", color="cobalt",cylinder_no=2,wheel_no=2,passenger_no=1,registration_status=True)


    print(newcar1.passenger_no)
    newcar1.add_passenger(2)
    print(newcar1.passenger_no)

    print(f"current registration status: {newcar1.registration_status}")
    
    
    #make a list of all of the vehicles
    vehicle_list = [newcar1,newcar2,newcar3,newbike1]

    #update the vehicle's registration status and watch the counter go up
    for vehicle in vehicle_list:
        captechMVA.update_registration_status(vehicle=vehicle)


main()