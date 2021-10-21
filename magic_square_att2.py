import numpy as np

def warn():

    print("\nInput is not valid! \n\nPlease ensure that you input a POSITIVE ODD number")

    user_input = int(input("\nPlease enter a positive odd number: \n\n"))

    return user_input


def magic_square(num):

    #variable declaration
    
    start_index = (num + 1)//2 
    col = start_index -1
    row = 0
    
    
    ## return a 2d list with  shape specified by param (to be user input)
    matrix = np.zeros((num, num))
    


    for i in range (1, (num*num) + 1):
        ## set first value at starting index in matrix
        matrix[row][col] = i

        ## move up and to the right in matrix
        col += 1
        row -= 1
        
        ## if row goes out of bounds set row to last value of range
        if row<0 and col<=num-1:
            
            row = num - 1

        # if both colum and row go out of bounds
        elif row<0 and col>num -1:

            row = row + 2
            col = num - 1
       
        # if the column val goes out of bounds and the row is within range
        # the value goes to the first column 
        elif col > num -1 and row <= num-1:

            col = 0

        # if the value on the matrix is not 0 and also within the range then
        # the 'move down' is done by reversing the previous ie moving the row down by 2 and the colum back by 1
        elif matrix[row][col] != 0 and col<=num-1 and row<=num-1 and row >= 0 and col>=0:

            row = row + 2
            col = col - 1

        else:
            continue

    return matrix
            
## this function will check that the sum of the rows, cols, diagonals are alike and that they are the same as the magic sum
## it will then print the result
def magic_sum_check(matrix, num):
    
    col1 = 0
    row1 = 0
    diag_1 = 0
    diag_2 = 0
    row_down = 0
    magic_sum = num*(num*num + 1)/2

    for cell_num in range(0, num):

        row1 += matrix[0][cell_num]
        col1 += matrix[cell_num][0]
        diag_1 += matrix[row_down][cell_num]
        diag_2 += matrix[row_down][num-1-cell_num]
        row_down += 1

    if row1 == col1 and diag_1 == diag_2 and row1 == diag_1 and diag_2 == magic_sum:
        print("\nMAGIC!!\n")
        print("Magic Sum => {} \n\nSum of row = {} \nSum of column = {} \nSum of diagonal 1 = {} \nSum of diagonal 2 = {}".format(magic_sum, row1, col1, diag_1, diag_2))           

    
def  main():

    instructions = """You (the user) are required to enter a positive odd number which will then be fed into the 'Magic Square' algorithm'. The program will output whether the calculation was successful("magic") or not("not magic")."""
    
    print("\nMagic Squares")

    print("\n", instructions)

    user_input = int(input("\nPlease enter a positive odd number: \n\n"))

    if user_input%2 == 0:
        user_input = warn()
        
    else:

        print("\nInput valid.  \n\nGenerating Magic Sqaure...\n")
            
        magic_matrix = magic_square(user_input)

        for j in range(user_input):
            print("|", end="")
                
            for k in range(user_input):
                print("%4d |" % magic_matrix[j][k], end="")
                        
            print()
                        
            for i in range(1, 6*user_input+1):
                print("-", end="")
                        
            print()

        magic_sum_check(magic_matrix, user_input)


main()












        
