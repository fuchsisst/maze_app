
# This function adds borders to all sides of the maze
def addBorderFunc(maze, width):
    maze.insert(0, ["#"]*(width-2))
    maze.append(["#"]*(width-2))
    
    # Insert a "#" symbol at the beginning and end of each line
    for row in maze:
        row.insert(0, "#")  # Insert at the beginning
        row.append("#")     # Insert at the end