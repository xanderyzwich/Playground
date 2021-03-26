from enum import Enum
from fractions import Fraction as frac 
from my_numbers import Fraction as my_frac
class VolumeUnit(Enum):
  # BASED ON FDA DEFINITIONS
	TEASPOON = 5 
	TABLESPOON = 15
	CUP = 240
	# BASED ON REFERENCE TO CUP
	PINT = 480
	QUART = 960
	GALLON = 3840
	
class Measurement:
	
	def __init__(self, amount, unit):
		if isinstance(unit,VolumeUnit):
			self.unit = str(unit).split(".")[1]
		else: self.unit = str(unit).upper
		self.amount = amount
		
		for name,member in VolumeUnit.__members__.items():
			if name == self.unit:
				self.mils = member.value * amount 
				self.unit = member.name
	
	def get(self,unit):
		if isinstance(unit,VolumeUnit):
			units = str(unit).split(".")[1]
		elif isinstance(unit,str):
			units = unit
		else:
			units = str(unit.name).upper
		for name,member in VolumeUnit.__members__.items():
			if name == units:
				temp = self.mils / member.value
				if temp % 1 != 0 : 
					if temp < 1:
						temp = frac(temp)
					else:
						print (my_frac(frac(temp)).reduce())
						temp = my_frac(frac(temp)).reduce()
				return temp
# testing script
# measure = Measurement(3,VolumeUnit.CUP)
# print (measure.amount, measure.unit," = ",measure.mils, "mL")
# print ( "    OR    ")
# for name,member in VolumeUnit.__members__.items():
# 	print (measure.get(member.name), name)


