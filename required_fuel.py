import math

airMoleMass = 28.97 # g/mol
rConst =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
ve = 1.0 # volumetric efficency
iat = 22 # °C | intake air temperature
cylDisp = 450 # cm3 | cylinder displacment
map = 0.8 # bar | mainfold absolute pressure

# air mass in grams
airMass = (ve * map * cylDisp) / (rConst * (iat + 273)) * airMoleMass
print(f"Air mass: {airMass} g")

fuelDensity = 0.740 # g/cm3
injectorFlowRate = 314 # cm3/min 
afr = 14.7 # air to fuel ratio; 14.7:1 is stoichiometric for petrol

# injector open time in miliseconds
pw = airMass / (afr * fuelDensity * injectorFlowRate) * 60 * 1000
print(f"Pulse width(naive): {pw} ms\n")


#-----------------------------------------------------------------------

# all consts as one
fuelConst = cylDisp * airMoleMass * 60 * 1000 / (afr * fuelDensity * injectorFlowRate * rConst)
print(f"Fuel const: {fuelConst}")

pw = (ve * map / (iat + 273)) * fuelConst
print(f"Pulse width(one const): {pw} ms\n")


#-----------------------------------------------------------------------

# int without division
iat_enrich = int((1 / (iat + 273)) * 256 * 256 * 256) # use lookup table in actual implemenation
print(f"Intake air temperature enrichment: {iat_enrich/4}")

pw = int(ve * map * iat_enrich * fuelConst) >> 22; # fixed point with 2 fractional bits
print(f"Pulse width(int, no div): {pw/4} ms\n")

