"""
Staircase
This is a staircase of size :

   #
  ##
 ###
####

Its base and height are both equal to .
It is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

Write a program that prints a staircase of size .
Function Description
    Complete the staircase function in the editor below.
    Print a staircase as described above.
Staircase has the following parameter(s):

    int n: an integer
"""


def staircase(size):
    return [print(' '*(size-i) + '#'*i) for i in range(1, size+1)]


def tree(size):
    [print(' '*(size-i) + '#'*(2*i+1)) for i in range(size)]


if __name__ == '__main__':
    staircase(4)
    staircase(10)
    tree(10)
    print(False == False in [False])

"""
OUTPUT: 
   #
  ##
 ###
####
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########
 #########
##########
          #
         ###
        #####
       #######
      #########
     ###########
    #############
   ###############
  #################
 ###################
"""