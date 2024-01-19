import random

# Length and width are determined by “cells”; when determining them,
# it is taken into account that borders are also included in these values
length = 10
width = 10

# A list that will contain the final labyrinth
maze = []

# Top border of the maze, the values do not change.
# Used only when displaying the end maze
top_border = ['#'] * width

maze.append(top_border)


def mazeGenerationAlgorithm(length, width, maze):
    for i in range(length - 1):
        
        # This variable stores the number from which the counting for subsets begins
        first_subset = 1

        # First row of the maze
        row_0 = [0] * (width - 2)
        row_1 = []

        # Add right and left borders
        row_1.append('#')

        # Subset generation. There is a "wall" between the sets
        i = 1
        while i < width - 2:
            if type(row_0[i]) == int:
                if bool(random.randint(0, 1)):
                    row_1.append(first_subset)
                    i = i+1
                else:
                    first_subset = first_subset + 1
                    row_1.append('#')
                    row_1.append(first_subset)
                    i = i+1
            

        row_1.insert(0, "#")

        # The second line is needed to display the lower borders
        row_2 = []

        # Lower borders generation
        for index in range(len(row_1) - 1):
            if row_1[index] == row_1[index + 1]:
                row_2.append('#')
            else:
                row_2.append(0)

        # This row is needed to pre-prepare the base for defining new subsets
        temp_row = []

        # Create a new row of the maze
        for index, value in enumerate(row_2):
            if type(row_1[index]) == type(value) == int:
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

        maze.append(row_1.copy())
        maze.append(row_2.copy())

    return maze


print(mazeGenerationAlgorithm(length, width, maze))

