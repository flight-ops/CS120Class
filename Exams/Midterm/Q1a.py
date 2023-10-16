#ideal gas law, p * v = n * R * T
#R is constant 8.4344
#n is constant 3 mol

#V = N R T / P

def volume_calculation(n,r,t,p):
    gas_volume = (n*r*t)/p  
    return gas_volume


def main():
    R_constant = float(8.4344)
    n_constant = float(3)
    gas_temp = float(input("What is the temperature of the gas?\t"))
    gas_pressure = float(input("What is the pressure of the gas?\t"))
    gas_volume = volume_calculation(n=n_constant, r= R_constant, t=gas_temp, p=gas_pressure)
    print("The volume of the gas is:", gas_volume)

main()