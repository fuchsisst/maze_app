import random

# Length and width are determined by “cells”; when determining them,
# it is taken into account that borders are also included in these values
length = 10
width = 10

def mazeGenerationAlgorithm(length, width):
    # A list that will contain the final labyrinth
    maze = []
    # Top border of the maze, the values do not change.
    # Used only when displaying the end maze
    top_border = ['#']*width
    
    # This variable stores the number from which the counting for subsets begins
    first_subset = 1
    
    # First row of the maze
    row_1 = []
    
    # Add right and left borders
    row_1.append('#')
    row_1.insert(0, "#") 
    
    # Subset generation. There is a "wall" between the sets
    def subsetGenerationFunc(row, first_subset):
        for i in range(width):
            if(type(i) == int):
                if (bool(random.randint(0, 1)) == 1):
                    row.append(first_subset)
                else:
                    first_subset = first_subset + 1
                    row.append('#')
                    row.append(first_subset)
            else:
                row.append('#')
        return row
            
    # for i in range(width):
    #     if(type(i) == int):
    #         if (bool(random.randint(0, 1)) == 1):
    #             row_1.append(first_subset)
    #         else:
    #             first_subset = first_subset + 1
    #             row_1.append('#')
    #             row_1.append(first_subset)
    #     else:
    #         row_1.append('#')
               
    row_1 = subsetGenerationFunc(row_1, first_subset)
    
    # The second line is needed to display the lower borders
    row_2 = []  
    
    # Lower borders generation
    for index, value in enumerate(row_1):
        if value == '#':
            row_2.append('#')
        else:
            if row_1[index] == row_1[index + 1]:
                row_2.append('#')
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
    # Why -2? Because we omit the value of the right border
    subset_value = temp_row[-2]
    
    # Defining new subsets. Assign each cell that is not included in any set its own unique set
    for index, value in enumerate(temp_row):
        if value == 0:
            value = subset_value + 1
            subset_value = value
            row_3.append(value)
        else:
            row_3.append(value)
      
