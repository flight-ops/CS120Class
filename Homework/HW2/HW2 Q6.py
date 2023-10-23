#gravitational potential energy calculator



def grab_inputs():
    mass_local = float(input("What is the mass of your object or particle in kg (kilograms)?\n"))
    height_local = float(input("What is the height of your object or particle in m (meters)?\n"))
    return mass_local,height_local

def check_inputs_for_zero(mass, height):
    if (mass ==0) or (height ==0):
        print("One of your mass or height values is zero!")
        return True
    else:
        return False

def calculate_mgh(m,g,h,zero_present_condition):
    if zero_present_condition == True:
        print("Gravitational potential energy is 0")
    else:
        U_g_local = round(m*g*h,2)
        print("Gravitational potential energy is",U_g_local,"Joules")
        

def main():
    # the g of mgh 
    g_constant = 9.8
    mass_main, height_main= grab_inputs()
    zero_present_condition = check_inputs_for_zero(mass_main,height_main)
    calculate_mgh(mass_main,height_main,g_constant,zero_present_condition)
    
main()