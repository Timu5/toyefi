import math

def fixed(number):
	return int(number * 1024)
	
def fixmul(a, b):
	return (a * b) >> 10 

air_mole_mass = 28.97 # g/mol
gas_const =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
ve = 1 # volumetric efficency
iat = 22 # °C | intake air temperature
disp = 450 # cm3 | cylinder displacment
map = 0.8 # bar | mainfold absolute pressure
fuel_density = 0.740 # g/cm3
injector_flow = 314 # cm3/min 
afr = 14.7 # air to fuel ratio; 14.7:1 is stoichiometric for petrol

fuel_const = disp * air_mole_mass * 60 * 100 / (afr * fuel_density * injector_flow * gas_const)
print(f"Fuel const: {fuel_const}")

iat_enrich = fixed((1 / (iat + 273)) * 1024) # use lookup table in actual implemenation
print(f"Intake air temperature enrichment: {iat_enrich}")

pw = fixmul(fixed(ve), fixed(map))
pw = fixmul(pw, fixed(fuel_const));
pw = fixmul(pw, iat_enrich) >> 10

print(f"Pulse width(int, no div): {pw/1024} ms")

max_rpm = int((1/(pw/1024))*60*1000)
print(f"Max RPM: {max_rpm}")
