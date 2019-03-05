import math

def calc_fuel(ve, map, iat, disp, afr, injector_flow):
	air_mole_mass = 28.97    # g/mol
	gas_const =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
	fuel_density = 0.740     # g/cm3

	# air mass in grams
	air_mass = (ve * map * disp) / (gas_const * (iat + 273)) * air_mole_mass
	
	# injector open time in miliseconds
	pw = air_mass / (afr * fuel_density * injector_flow) * 60 * 100

	return pw

print(calc_fuel(0.8, 1, 22, 500, 14.7, 315), "ms")
