class Offsetter:
	numericOffset=0
	
	def __init__(self, offset):
		self.numericOffset = offset
	
	def setOff(self, input_int):
		return (( input_int + self.numericOffset ) % 10)
	
	def setOn(self, input_int):
		return (( input_int + (10 - self.numericOffset) ) % 10)
	
	def stringOffset(self,input_string):
		if str(input_string).isnumeric() :
			return ''
		output_string = ''
		for s in input_string:
			output_string = output_string + str(setOff(s))
		return output_string

offset = input("Please enter the desired offset:  ")
os = Offsetter(offset)
# for i in range(9):
# 	print os.setOff(i)
print os.stringOffset('0123456789')
	
# class Encoder:
# 	encoding
# 	normalizing

# 	def __init__(self, fileName):
# 		file_object = open(fileName,'r')
# 		normal = file_object.read(0)
# 		if (normal.lower == 'normalize,yes'):
# 			normalizing=true
# 		else:
# 			normalizing=false
# 		self.encoding.append	

