# Magic square program
# The program will take in a user input that should be a positive odd number
# The code's output verifies that the 'magic square'  calculation is correct or not, 
# while verifying if the user's input is correct as well
# In the square format: each row, column and diagonals should add up to the same number
# Python program to generate magic square
# code inspired from: https://www.codesansar.com/python-programming-examples/generate-magic-square.htm

import sys
import numpy as np


def warn():

    print("\nInput is not valid! \n\nPlease ensure that you input a POSITIVE ODD number")

    user_input = int(input("\nPlease enter a positive odd number: \n\n"))

    return user_input

def magic_square(num):

    magic_sum = num((num*num + 1)/2)
    row_matrix = []
    col_matrix = []
    magic_matrix = 

    for i in range(1, magic_sum):
        
        
        

    print("Magic!!\n")
    print("Generated Magic Square is: \n")

    for j in range(num):
        print("|", end="")
            
        for k in range(num):
            print("%4d |" % magic[j][k], end="")
                
        print()
                
        for i in range(1, 6*num+1):
            print("-", end="")
                
        print()
        

def  main():

    instructions = """
 You (the user) are required to enter a positive odd number which will then be fed into the 'Magic Square' algorithm'. The program will output whether the calculation was successful("magic") or not("not magic")."""
    
    # variable declaration
    magic = False
    matrix = []
    
    print("\nMagic Squares")

    print("\n", instructions)

    user_input = int(input("\nPlease enter a positive odd number: \n\n"))

    if user_input%2 == 0:
        user_input2 = warn()

        magic_square(user_input2)
        
    else:
        print("\nInput valid.  Generating Magic Sqaure...\n")
        magic_square(user_input)

main()

