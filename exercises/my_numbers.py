import math
class MathTool:
	#	MathTool class is a stateless utility class
	
	@staticmethod
	# Returns prime factorization of the input_num
	def factor(input_num):
		remaining = input_num
		factor_list = []
		prime_list=MathTool.getPrimes(math.ceil(math.sqrt(input_num)))
		for prime in prime_list:
			while remaining % prime ==0:
				factor_list.append(prime)
				remaining = remaining / prime
		if remaining !=1: factor_list.append(remaining)
		return sorted(factor_list)
	
	@staticmethod
	#	Returns paired factors of input_num
	def getFactors(input_num):
		factors_list = [input_num]
		if input_num!=1: factors_list.append(1)
		for index in range(2,input_num):
			if input_num % index == 0 and index not in factors_list: 
				factors_list.append(index)
				if index**2 != input_num: 
					factors_list.append(input_num/index)
		return sorted(factors_list)
	
	@staticmethod
	def getPrimes(max_num):
		prime_list = [2]
		index = 3
		while index < max_num:
			isPrime = True
			for prime in prime_list:
				if index % prime == 0: 
					isPrime = False
					break
			if isPrime: prime_list.append(index)
			index+=1
		return sorted(prime_list)
	
	@staticmethod
	def findCommon(list_one,list_two):
		output_list=[]
		for number in list_one:
			if number in list_two:	output_list.append(number)
		return sorted(output_list)
	
	@staticmethod
	# Greatest Common Divisor
	def gcd(input_one,input_two):
		if input_one ==0 or input_two == 0: return 0
		elif input_one == 1 or input_two == 1: return 1
		divisor = 1
		for number in MathTool.findCommon(MathTool.factor(input_one), MathTool.factor(input_two)):
			divisor*=number
		return divisor
	
	@staticmethod
	#	Least Common Multiple
	def lcm(input_one,input_two):
		if input_one % input_two == 0:
			return input_one
		if input_two % input_one == 0:
			return input_two
		list_one=[]
		list_two=[]
		for i in range(1,input_two+1):
			list_one.append(input_one * i)
		for i in range(1,input_one+1):
			list_two.append(input_two * i)
		list_common = MathTool.findCommon(list_one,list_two)
		return list_common.pop(0)
	
		multiples=[]
	@staticmethod
	#	Sieve of Eratosthenes
	def sievePrimes(max_num):
		prime_list=[]
		multiples=[]
		check_num=2
		while check_num <= math.ceil(math.sqrt(max_num)):
			if check_num not in multiples:
				multiple=check_num**2 
				while multiple <= max_num:
					if multiple not in multiples:
						multiples.append(multiple)
					multiple+=check_num
			check_num+=1
		for number in range(1,max_num+1): 
			if number not in multiples: 
				prime_list.append(number)
		return prime_list
	
	@staticmethod
	def comparePrimes(max_num):
		print ("testing sievePrimes v getPrimes for max_num=",max_num)
		from datetime import datetime as dt
		before = dt.now()
		print ("Sieve")
		print (MathTool.sievePrimes(max_num))
		sieve_time=dt.now()-before
		print (sieve_time)
		before = dt.now()
		print ("Primes")
		print (MathTool.getPrimes(max_num))
		prime_time=dt.now()-before
		print (prime_time)
		if sieve_time < prime_time: 
			print ("Sieve WINS by",prime_time-sieve_time)
		elif prime_time < sieve_time: 
			print ("getPrimes WINS by",sieve_time-prime_time)
		else: 
			print ("there is a TIE at",sieve_time)

class Fraction:
	
	def __init__(self,input_numerator,input_denominator=1):
		self.numerator=input_numerator
		self.denominator=input_denominator
		self.value = self.numerator / self.denominator
	
	def setNumerator(self,input_numerator):
		self.numerator=input_numerator
		self.setValue()
	
	def setDenominator(self,input_denominator):
		self.denominator=input_denominator
		self.setValue()
	
	def setValue(self): # triggers value to be corrected after numerator or denominator are changed
		self.value = self.numerator / self.denominator
	
	def __str__(self):
		return str(self.numerator) +"/" +str(self.denominator)
	
	def add(self, other_fraction):
		if self.denominator != other_fraction.denominator:
			new_denom=MathTool.gcd(self.denominator,other_fraction.denominator)
			scale_self=new_denom/self.denominator
			scale_other=new_denom/other_fraction.denominator
			result = Fraction(scale_self*self.numerator + scale_other*other_fraction.numerator,new_denom)
			return result.reduce()
		else:
			return Fraction(self.numerator+other_fraction.numerator,self.denominator).reduce()
	
	def subtract(self, other_fraction):
		return self.add(other_fraction.multiply(Fraction(-1))).reduce()
	
	def multiply(self, other_fraction):
		return Fraction(self.numerator * other_fraction.numerator, self.denominator * other_fraction.denominator).reduce
	
	def divide(self, other_fraction):
		return self.multiply(other_fraction.inverse()).reduce()
	
	def inverse(self):
		return Fraction(self.denominator,self.numerator)
	
	def reduce(self):
# 		print ("Reducing", self)
		if self.numerator in [0,1]: 
			return self
		elif self.numerator % self.denominator == 0 : #if integer 
			self = MixedNumber(self.numerator / self.denominator,Fraction(0,1))
			return self
		elif self.value >= 1: #if mixed number 
			return MixedNumber(self.numerator/self.denominator,Fraction(self.numerator%self.denominator,self.denominator))
		else: # otherwise insure fraction is reduced
			new_denom = MathTool.gcd(self.numerator, self.denominator)
			self = Fraction(self.numerator/new_denom,self.denominator/new_denom)
			return self

class MixedNumber:
	
	def __init__(self,input_integer,input_fraction):
		self.integer_part=input_integer
		self.fraction_part=input_fraction
		self.value = input_integer + input_fraction.value 
	
	def reduce (self):
# 		print ("Reducing",self)
		output_fraction = self.fraction_part.reduce()
		output_integer = self.integer_part
		if output_fraction.value >= 1:
			output_integer += output_fraction.reduce().integer_part
			output_fraction = output_fraction.reduce().fraction_part
		self = MixedNumber(output_integer,output_fraction)
		return self
	
	def	add(self,input_mixed):
		output_integer = self.integer_part+input_mixed.integer_part
		output_fraction = self.fraction_part.add(input_mixed.fraction_part)
		output_mixed = MixedNumber(output_integer,output_fraction).reduce()
		return output_mixed
	
	def subtract(self,input_mixed):
		return self.add(input_mixed.multiply(-1)).reduce
	
	def multiply(self,input_mixed):
		return self.toFraction().multiply(input_mixed.toFraction()).reduce()
	
	def divide(self,input_mixed):
		return self.toFraction().divide(input_mixed.toFraction()).reduce()
	
	def toFraction(self):
		return FractioN(self.integer_part*self.denominator + self.numerator,self.denominator)
	
	def __str__(self):
		output_string = ""
		if self.integer_part > 0:
			output_string = output_string +str(self.integer_part)
		if self.integer_part > 0 and self.fraction_part.numerator > 0:
			output_string = output_string +" and "
		if self.fraction_part.numerator > 0:
			output_string = output_string +str(self.fraction_part) 
		return  output_string


	
test = MixedNumber(1,Fraction(1,2))
thing = MixedNumber(0,Fraction(1,2))
print (test," + ",thing," = ", str(test.add(thing)))