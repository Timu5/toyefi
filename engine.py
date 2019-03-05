
class Engine:
	
	def __init__(self):
		self.disp = 500
		self.injector_flow = 315
		
		self.rpm = 0
		
		self.map = 1
		self.iat = 22
		self.cht = 90
		
		self.ve = 0.8
		self.afr = 14.7
		self.warm = 1	
		
	def read_adc(self):
		# in real implementation we would sample each adc channel
		pass
		
	def convert_raw(self):
		pass
	
	def calc_vars(self):
		pass
	
	def calc_fuel(self):
		air_mole_mass = 28.97    # g/mol
		gas_const =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
		fuel_density = 0.740     # g/cm3

		# air mass in grams
		air_mass = (self.ve * self.map * self.disp) / (gas_const * (self.iat + 273)) * air_mole_mass
	
		# injector open time in miliseconds
		pw = air_mass / (self.afr * fuel_density * self.injector_flow) * 60 * 100

		return pw