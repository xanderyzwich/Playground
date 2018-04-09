class Offsetter:
	numericOffset=0
	
	def __init__(self, offset):
		self.numericOffset = int(offset)
	
	def setOff(self, input_int):
		return (( int(input_int) + self.numericOffset ) % 10)
	
	def setOn(self, input_int):
		return (( input_int + (10 - self.numericOffset) ) % 10)
	
	def stringOffset(self,input_string):
		output_string = ''
		for s in input_string:
			print output_string
			input_int = self.char2int(s)
			output_string = output_string + str(self.setOff( input_int ))
		return output_string
	
	def char2int(self,input_char):
		return {
			'0': 0,
			'1': 1,
			'2': 2,
			'3': 3,
			'4': 4,
			'5': 5,
			'6': 6,
			'7': 7,
			'8': 8,
			'9': 9,
		}.get(input_char,0)


# offset = input("Please enter the desired offset:  ")
os = Offsetter(5)
# print os.setOff('0')
# for i in range(9):
#  	print os.setOff(i)
print os.stringOffset('0123456789')
# print os.char2int('0')
	
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

