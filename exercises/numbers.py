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
				if index**2 != input_num: factors_list.append(input_num/index)
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
		divisor = 1
		for number in MathTool.findCommon(MathTool.factor(input_one), MathTool.factor(input_two)):
			divisor*=number
		return divisor
	
	@staticmethod
	#	Least Common Multiple
	def lcm(input_one,input_two):
		if input_one % input_two == 0: return input_one
		if input_two % input_one == 0: return input_two
		list_one=[]
		list_two=[]
		for i in range(1,input_two+1):	list_one.append(input_one * i)
		for i in range(1,input_one+1):	list_two.append(input_two * i)
		list_common = MathTool.findCommon(list_one,list_two)
		return list_common.pop(0)

# for i in range(1,13):
# 	print '%(index)s -> %(factors)s' %{ 'index':i, 'factors':MathTool.getFactors(i)	}
print MathTool.lcm(12,18)

