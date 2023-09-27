#Create a function that spits out a value for force given a mass and an acceleration.
# F = MA
beep_boop_bop = 4
def main():
    #nice message for user
    print("\nThis tool is meant to help you calculate the force imparted on an object or particle.")
    #gather user input
    user_input_mass = input("\nWhat is the mass of your object in kilograms?")
    user_input_acceleration = input("\nWhat is the acceleration of your object in meters per second squared?")
        
    #define function for calculating force
    def calculate_force(mass, acceleration):
        #if either provided value is 0, don't perform a calculation and just return 0
        if(mass == 0 or acceleration == 0):
            #tell user that their object is in constant acceleration
            print("\n ----- Your object is experiencing constant acceleration or is at rest! -----")
            return 0
        else:
            #perform calculation and return the force value
            force = mass * acceleration
            return force


    print("\nThe force imparted is", calculate_force(float(user_input_mass),float(user_input_acceleration)), "Newtons")

while beep_boop_bop == 4:
    main()