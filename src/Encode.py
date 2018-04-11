# Adjusts numerical digits by a specified amount 
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

# Converts char to ascii
class Encoder:
	def string2ascii (self, input_string):
		print len(input_string)
		return_list = []
		for i in range(0,len(input_string)):
			return_list.insert(i,self.char2ascii(input_string[i]))
		return return_list
	
	def char2ascii(self, input_char):
		return ord(input_char)

# Converts ascii to char
class Decoder:
	def string2ascii (self, input_list):
		print len(input_list)
		return_string = ''
		for i in input_list:
			print i
			print self.char2ascii(i)
			return_string= return_string + self.char2ascii(i)
		return return_string
	
	def char2ascii(self, input_int):
		return chr(input_int)