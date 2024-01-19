import random

# Length and width are determined by “cells”; when determining them,
# it is taken into account that borders are also included in these values
length = 10
width = 10

# A list that will contain the final labyrinth
maze = []

    
def mazeGenerationAlgorithm(length, width, maze):
    
    # Top border of the maze, the values do not change.
    # Used only when displaying the end maze
    top_border = ['#']*width 
    
    maze.append(top_border) #10
     
    # This variable stores the number from which the counting for subsets begins
    first_subset = 1
    
    
    # First row of the maze
    row_0 = [0]*(width-2) # 8
        
    row_1 = []
    # Subset generation. There is a "wall" between the sets
      
    for i in range(length - 1):
        if row_1:
            row_first_subset = row_1[0]  
        else:
            row_first_subset = 1
            
        # for i in row_0:
        #     if(type(i) == int):
        #         if (bool(random.randint(0, 1)) == 1):
        #             row_1.append(first_subset)
        #         else:
        #             first_subset = first_subset + 1
        #             row_1.append('#')
        #             row_1.append(first_subset)
        #     else:
        #         row_1.append('#')
               
        for i, value in enumerate(row_0):
            if not row_1:
                if bool(random.randint(0, 1)):
                    row_1.append(first_subset)
                else:
                    first_subset = first_subset + 1
                    row_1.append('#')
                    row_1.append(first_subset)
            
                # Checking the length of row_1 and ending the loop if it reaches the desired value
                if len(row_1) > len(row_0):
                    del row_1[-(len(row_1)-len(row_0)):]
                    break
            else:
                if bool(random.randint(0,1)):
                    row_1[i] = row_first_subset
                else:
                    if i+2 <= len(row_1):
                        row_first_subset = row_1[i+1]
                        row_1[i] = '#'
                        #row_1[i+2] = row_first_subset
                    else:
                        break
                    
                if len(row_1) > len(row_0):
                    del row_1[-(len(row_1)-len(row_0)):]
                    break   
        for i, value in enumerate(row_0):
            if bool(random.randint(0, 1)):
                row_1.append(first_subset)
            else:
                first_subset = first_subset + 1
                row_1.append('#')
                row_1.append(first_subset)
            
                # Checking the length of row_1 and ending the loop if it reaches the desired value
            if len(row_1) > len(row_0):
                del row_1[-(len(row_1)-len(row_0)):]
                break
                       
    
        # # The second line is needed to display the lower borders
        # row_2 = []  
    
        # # Lower borders generation
        # for index, value in enumerate(row_1):
        #     if value == '#':
        #         row_2.append('#')
        #     else:
        #         if row_1[index] == row_1[index + 1]:
        #             row_2.append('#')
        #         else:
        #             row_2.append(0)
        
        # The second line is needed to display the lower borders
        row_2 = []  

        # Lower borders generation
        for index, _ in enumerate(row_1):
            if row_1[index] == '#':
                row_2.append('#')
            else:
                if index != len(row_1)-1:
                    if row_1[index] == row_1[index + 1]:
                        row_2.append('#')
                    else:
                        row_2.append(0)
                else:
                    row_2.append(0)


        # This row is needed to pre-prepare the base for defining new subsets
        temp_row = []

        # Create a new row of the maze
        for index, value in enumerate(row_2):
            if(type(row_1[index]) == type(value) == int):
                temp_row.append(row_1[index])
            else:
                temp_row.append(0)
    
        # Instead of zeros in this line, we will define new subsets    
        row_3 = []
    
        # Get the last value of a subset. 
        subset_value = max(temp_row)
    
        # Defining new subsets. Assign each cell that is not included in any set its own unique set
        for index, value in enumerate(temp_row):
            if value == 0:
                value = subset_value + 1
                subset_value = value
                row_3.append(value)
            else:
                row_3.append(value)
                
        maze.append(row_1)
        maze.append(row_2)
        
        row_1 = row_3

    return maze


print(mazeGenerationAlgorithm(length, width, maze))