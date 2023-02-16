# Import modules
import random

def minefield_maker(n_x_n):
    # Generate array of random '-' or '#', 2:1 ratio, and display to user
    chars = '--#'
    array = [[(random.choice(chars)) for i in range(n_x_n)] for j in range(n_x_n)]
    print(f"\nHere is your {n_x_n} x {n_x_n} minefield:\n")
    for i in range(len(array)):
        print(' '.join(str(e) for e in array[i]))

    # Add zeros to the start and end of each line
    array_plus = []
    for i in range(len(array)):
        array[i].append(0)
        a = [0] + array[i]
        array_plus.append(a)

    # Add zeros to the 'top' and 'bottom'
    input = [[0]*(n_x_n + 2)]             
    for i in range(len(array_plus)):
        input.append(array_plus[i])
    input.append([0]*(n_x_n + 2))

    # Convert all "-" to 0 integers
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == "-":
                input[row][col] = 0
        
    # Adding +1 to each coordinate neighbouring input[x][y]. Range from indices [1] to [n-1]
    for x in range(1,len(input)-1):
        for y in range(1,len(input[x])-1):
            if type(input[x][y]) == int:
                if type(input[x][y+1]) != int:
                    input[x][y] += 1
                if type(input[x][y-1]) != int:
                    input[x][y] += 1
                if type(input[x+1][y]) != int:
                    input[x][y] += 1
                if type(input[x-1][y]) != int:
                    input[x][y] += 1
                if type(input[x+1][y+1]) != int:
                    input[x][y] += 1
                if type(input[x-1][y-1]) != int:
                    input[x][y] += 1
                if type(input[x+1][y-1]) != int:
                    input[x][y] += 1
                if type(input[x-1][y+1]) != int:
                    input[x][y] += 1

    # Removing border zeroes
    minefield = []
    for x in range(1,len(input)-1):
        output = input[x]
        output.pop()
        output.pop(0)
        minefield.append(output)

    # Printing final output
    print("\nHere is your minefield indicating the number of mines adjacent to each \"-\" :\n")
    for i in range(len(minefield)):
        print(' '.join(str(e) for e in minefield[i]))
    print("\n")

# Getting size of array
while True:
    array_size = int(input("Size of n x n minefield: "))
    if array_size > 50:
        print("Too big!")
    else:
        break

#Calling the function
minefield_maker(array_size)
