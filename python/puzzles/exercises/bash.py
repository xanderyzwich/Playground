import os
import sys 

# this works to pull the arguments of the script called from command line
# os.system(" ".join(sys.argv[1:]))

# this works with the init arg string
class Bash:
	def __init__(self, args):
		os.system(args)