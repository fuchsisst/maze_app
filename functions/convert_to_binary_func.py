
# This function is responsible for representing the maze in binary form.
def convertToBinaryFunc(maze):
    for row in maze:
        for i in range(len(row)):
            if isinstance(row[i], int):
                row[i] = 1
            if row[i] == "#":
                row[i] = 0