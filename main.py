from engine import Engine

engine = Engine()
engine.read_adc()
engine.convert_raw()
engine.calc_vars()
print(engine.calc_fuel(), "ms")
