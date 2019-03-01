import math

airMoleMass = 28.97 # g/mol
rConst =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
ve = 1.0 # volumetric efficency
iat = 22 # °C | intake air temperature
cylDisp = 450 # cm3 | cylinder displacment
map = 0.02 # bar | mainfold absolute pressure

# air mass in grams
airMass = (ve * map * cylDisp) / (rConst * (iat + 273)) * airMoleMass
print(airMass)

fuelDensity = 0.740 # g/cm3
injectorFlowRate = 314 # cm3/min 
afr = 14.7 # air to fuel ratio; 14.7:1 is stoichiometric for petrol

#injector open time in miliseconds
pw = airMass / (afr * fuelDensity * injectorFlowRate) * 60 * 1000
print(pw)
