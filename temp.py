import random
from PIL import Image

# Length and width are determined by “cells”; when determining them,
# it is taken into account that borders are also included in these values
length = 100
width = 100

# A list that will contain the final labyrinth
maze = []

    
def mazeGenerationFunc(length, width, maze):
    
    # Top und bottom borders of the maze, the values do not change.
    # Used only when displaying the end maze
    top_bottom_border = ['#']*(width-4) 
    print(top_bottom_border)
    maze.append(top_bottom_border)
     
    
    # First row of the maze
    row_0 = list(range(1, width-1)) # For example, [1, 2, 3, 4, 5, 6, 7, ...]
        
    
    # Subset generation funtion. There is a "wall" between the sets 
    def subsetGenerationFunc(row):
        row_first_subset = row[0]
        
        for i, value in enumerate(row):
            if bool(random.randint(0,1)):
                if i < len(row)-1: 
                    row[i+1] = row_first_subset
                else:
                    break
            else:
                if i < len(row)-1:
                    row[i+1] = '#'
                else:
                    break
                if i < len(row)-2:
                    row_first_subset = row[i+2]
                else:
                    break
        
        return row
    
    # Lower borders generation function.
    def lowerBorderGenerationFunc(row_1):
        row_2 = []
        for i, _ in enumerate(row_1):
            if row_1[i] == '#':
                row_2.append('#')
            else:
                if i != len(row_1)-1:
                    if row_1[i] == row_1[i + 1]:
                        if bool(random.randint(0,1)):
                            row_2.append('#')
                        else:
                            row_2.append(0)
                    else:
                        row_2.append(0)
                else:
                    row_2.append(0)
        return row_2
    
    def newLineGenerationFinc(row_1, row_2):
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
        
    # If the length is even
    if length - 2 % 2 == 0:  
        for i in range(0, length - 2, 2):
            row_1 = subsetGenerationFunc(row_0)           
        
            # The second line is needed to display the lower borders
            row_2 = lowerBorderGenerationFunc(row_1)  
            
            row_3 = newLineGenerationFinc(row_1, row_2)
            
            maze.append(row_1)
            maze.append(row_2)
            
            row_0 = row_3          
    else:
        for i in range(0, length - 3, 2):
            row_1 = subsetGenerationFunc(row_0)           
        
            # The second line is needed to display the lower borders
            row_2 = lowerBorderGenerationFunc(row_1)  
            
            row_3 = newLineGenerationFinc(row_1, row_2)
            
            maze.append(row_1)
            maze.append(row_2)
            
            row_0 = row_3
            
    maze.append(top_bottom_border) #10
    
    # Добавим боковые границы лабиринта
    # Вставляем символ "#" в начало и конец каждого подсписка
    for sublist in maze:
        sublist.insert(0, "#")  # Вставляем в начало
        sublist.append("#")     # Вставляем в конец
    
    for sublist in maze:
        for i in range(len(sublist)):
            if isinstance(sublist[i], int):
                sublist[i] = 0
            if sublist[i] == '#':
                sublist[i] = 1
    
    return maze


mazeFinish = mazeGenerationFunc(length, width, maze)
# Вывод результата
for sublist in mazeFinish:
    print(''.join(map(str, sublist)))

# Пример списка из подсписков (0 - белый, 1 - черный)
image_data = mazeFinish

# Размеры изображения
width = len(image_data[0])
height = len(image_data)

# Создание изображения
image = Image.new("1", (width, height))  # "1" означает двоичный режим (черно-белый)

# Заполнение изображения данными из списка
for y in range(height):
    for x in range(width):
        pixel_value = image_data[y][x]
        image.putpixel((x, y), pixel_value)

# Сохранение изображения
image.save("output.png")