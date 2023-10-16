#ideal gas law, p * v = n * R * T
#R is constant 8.4344
#n is constant 3 mol
#output pressure given temperature and volume
#P = nRT/V

def pressure_calculation(n,r,t,v):
    gas_pressure = (n*r*t)/v  
    return gas_pressure

def main():
    R_constant = float(8.4344)
    n_constant = float(3)
    gas_temp = float(input("What is the temperature of the gas?\t"))
    gas_volume = float(input("What is the volume of the gas?\t"))
    gas_pressure = pressure_calculation(n=n_constant, r= R_constant, t=gas_temp, v=gas_volume)
    print("The pressure of the gas is:", gas_pressure)

main()