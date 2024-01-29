import random

# This is a link to a more detailed description of Euler's algorithm:
# http://www.neocomputer.org/projects/eller.html

# A function that implements the Euler algorithm for generating a labyrinth.
# Returns the finished maze.
def mazeGenerationFunc(length, width, maze):
        
    # Row of the maze without walls.
    # Each number in the list indicates its own unique subset.
    row_0 = list(range(1, width-1)) # For example, [1, 2, 3, 4, 5, 6, 7, ...]
        
    
    # Subset generation funtion. There is a "wall" between the sets.
    # After using this function, the maze line will look something like this:
    # [1, 1, #, 3, 3, 3, #, ..., n|# ]
    def subsetGenerationFunc(row):
        
        # This variable stores the number of the first subset.
        row_subset = row[0] # For example, row[0] = 1
        
        # In this cycle, we go through each element of the labyrinth line
        # and determine in which places the walls will stand.
        for i in range(0, len(row), 2):
            if bool(random.randint(0,1)):
                if i < len(row)-1: 
                    row[i+1] = row_subset
                    row[i+2] = row_subset
                else:
                    break
            else:
                if i < len(row)-1:
                    row[i+1] = '#'
                    row_subset = row[i+2]
                else:
                    break
        return row
    
    # Lower borders generation function.
    # After using this function, maze lines will look something like this:
    # [1, 1, #, 3, 3, 3, #, ..., n|# ]
    # [#, 0, #, #, #, 0, #, ..., 0|# ]
    def lowerBorderGenerationFunc(row_1):
        
        # We create lists for storing unique numbers and their quantities
        unique_digits = []
        digit_counts = []

        current_digit = None
        count = 0

        for i in row_1:
            if isinstance(i, int):
                if i == current_digit:
                    count += 1
                else:
                    if current_digit is not None:
                        unique_digits.append(current_digit)
                        digit_counts.append(count)
                    current_digit = i
                    count = 1

        # Add the last digit and its quantity to the lists
        if current_digit is not None:
            unique_digits.append(current_digit)
            digit_counts.append(count)
    
        row_2 = []
        has_zero = False  # Flag to track the presence of 0 in the current subset
        count_zeros = 0  # Counter of consecutive zeros

        for i, value in enumerate(row_1):
            if value == '#':
                row_2.append('#')
                has_zero = False  # Reset the flag when a '#' character is detected
                count_zeros = 0  # Resetting the counter of consecutive zeros
            else:
                if i < len(row_1) - 1:
                    if value == row_1[i + 1]:
                        if not has_zero:  # Checking if there is already 0 in the current subset
                            if count_zeros >= 2:  # If there are 2 or more zeros in a row
                                row_2.append('#')  # Add two '#' characters
                                #row_2.append('#')
                                has_zero = True  # Set the flag that 0 has already been added
                                count_zeros = 0  # Resetting the counter
                            else:
                                row_2.append('#')  # If there are less than 2 zeros in a row, add one '#' symbol
                                has_zero = True  # Set the flag that 0 has already been added
                                count_zeros = 1  # Increase the counter by 1
                        else:
                            row_2.append('#')  # If there is already 0, add '#'
                            count_zeros += 1  # We increase the counter of consecutive zeros
                    else:
                        row_2.append(0)
                        has_zero = False  # We reset the flag since 0 was added
                        count_zeros = 0  # Resetting the counter
                else:
                    row_2.append(0)

        return row_2

    # This function, roughly speaking, prepares the next line
    # to apply the function subsetGenerationFunc()
    # After using this function, maze lines will look something like this:
    # [1, 1, #, 3, 3, 3, #, ..., n|# ]
    # [#, 0, #, #, #, 0, #, ..., 0|# ]
    # [n + 1, 0, n + 2, n + 3, n + 4, 0, n + 5, ..., n + k|0 ]
    def newLineGenerationFunc(row_1, row_2):
        # This row is needed to pre-prepare the base for defining new subsets
        temp_row = []
        
        # Create a new row of the maze
        for i, value in enumerate(row_2):
            if(type(row_1[i]) == type(value) == int):
                temp_row.append(row_1[i])
            else:
                temp_row.append(0)
        
        # Instead of zeros in this line, we will define new subsets    
        row_3 = []
        
        # Get the last value of a subset. 
        subset_value = max(temp_row)
        
        # Defining new subsets. Assign each cell that is not included in any set its own unique set
        for _, value in enumerate(temp_row):
            if value == 0:
                value = subset_value + 1
                subset_value = value
                row_3.append(value)
            else:
                row_3.append(value)
                
        return row_3
        
    # Maze generation cycle
    for i in range(0, length - 3, 2):
        row_1 = subsetGenerationFunc(row_0)           
        
        # The second line is needed to display the lower borders
        row_2 = lowerBorderGenerationFunc(row_1)  
            
        row_3 = newLineGenerationFunc(row_1, row_2)
            
        maze.append(row_1)
        maze.append(row_2)
            
        row_0 = row_3
               
    return maze

# The output maze will look something like this:
# [1, 1, #, 3, 3, 3, #, ..., n|# ]
# [#, 0, #, #, #, 0, #, ..., 0|# ]
# [..............................]
# [∀n*r ... , #, (∀n+1)*r ... , #, ...., (∀n+k)*r|#], where r - random number
# [#*(r-1), 0, #, ..., #*(r-1)|0|# ]