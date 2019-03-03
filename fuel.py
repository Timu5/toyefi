import math

air_mole_mass = 28.97 # g/mol
gas_const =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
ve = 0.8 # volumetric efficency
iat = 22 # °C | intake air temperature
disp = 450 # cm3 | cylinder displacment
map = 1.6 # bar | mainfold absolute pressure

# air mass in grams
air_mass = (ve * map * disp) / (gas_const * (iat + 273)) * air_mole_mass
print(f"Air mass: {air_mass} g")

fuel_density = 0.740 # g/cm3
injector_flow = 314 # cm3/min 
afr = 14.7 # air to fuel ratio; 14.7:1 is stoichiometric for petrol

# injector open time in miliseconds
pw = air_mass / (afr * fuel_density * injector_flow) * 60 * 100
print(f"Pulse width(naive): {pw} ms\n")


#-----------------------------------------------------------------------

# all consts as one
fuel_const = disp * air_mole_mass * 60 * 100 / (afr * fuel_density * injector_flow * gas_const)
print(f"Fuel const: {fuel_const}")

pw = (ve * map / (iat + 273)) * fuel_const
print(f"Pulse width(one const): {pw} ms\n")
