# This is a practice of string excercises implemented functionally
class StringTool:
	
	# reverse a string
	@staticmethod
	def reversed(input_string):
			return "".join(reversed(input_string))

	# check if a string is a palindrome 
	@staticmethod
	def isPalindrome(input_string):
		return (reversed(input_string).lower() == input_string.lower())
	@staticmethod
	def testPalindrom(input_string):
		return "%(string)s == %(reverse)s is %(truth)s" % { 'string':input_string,'reverse':StringTool.reversed(input_string),'truth':StringTool.isPalindrome(input_string) }
	
	# count the number of words in a string 
	@staticmethod
	def countWords(input_string):
		return len(input_string.split(' '))
	
	# count vowels in a string
	@staticmethod
	def isVowel(input_string, index):
		return input_string.lower()[index] in 'aeiou'
	@staticmethod
	def countVowels(input_string):
		count=0
		for i in range(len(input_string)-1):
			if StringTool.isVowel(input_string,i): count += 1
		return count
	
	# pig latin
	@staticmethod
	def startVowel(input_string):
		#one way
		#return StringTool.isVowel(input_string,0)
		#another way 
		if StringTool.firstVowel(input_string) == 0: return True
		else: return False 
	@staticmethod
	def firstVowel(input_string):
		for i in range(len(input_string)):
			if StringTool.isVowel(input_string,i): return i
	