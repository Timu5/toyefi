from lookup import *

class Engine:
	
	def __init__(self):
		# const
		self.disp = 500 # cc
		self.injector_flow = 315 # cc/min
		self.injector_deadtime = 1 # ms
		
		# tables
		self.table_ve = Table2D()
		self.table_warm = Table1D()
		self.table_ign = Table2D()
		self.table_afr = Table2D()
		
		# data from sensors
		self.map = 1 # bar
		self.iat = 22 # °C
		self.cht = 90 # °C
		self.o2 = 1 # lamda
		
		# calculated variables
		self.rpm = 1000
		self.ve = 0.8
		self.afr = 14.7
		self.warm = 1 # warmup enrichment
		self.pw = 0 # injector puslewidth
		self.adv = 0 # ignition advance
		
	def read_adc(self):
		# in real implementation we would sample each adc channel
		pass
		
	def convert_raw(self):
		# convert raw adc reading into smth more usable
		pass
	
	def calc_vars(self):
		self.ve = lookup_2D(self.table_ve, self.rpm, self.map)
		self.warm = lookup_1D(self.table_warm, self.cht)
		self.afr = lookup_2D(self.table_aft, self.rpm, self.map)
	
	def calc_fuel(self):
		air_mole_mass = 28.97    # g/mol
		gas_const =  8.314459848 # (cm3*bar)/(mol*K) | gas constant
		fuel_density = 0.740     # g/cm3

		# air mass in grams
		air_mass = (self.ve * self.map * self.disp) / (gas_const * (self.iat + 273)) * air_mole_mass
	
		# injector open time in miliseconds
		base_pw = air_mass / (self.afr * fuel_density * self.injector_flow) * 60 * 100

		# final pulse width is calulated from base pulsewidth, enrichments and injector deadtime
		self.pw = base_pw * self.warm + self.injector_deadtime
		
		return self.pw
		
	def calc_ign(self):
		self.adv = lookup_2D(self.table_ign, self.rpm, self.map)
