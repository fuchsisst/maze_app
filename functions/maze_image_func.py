from PIL import Image

# This function takes the binary form of the labyrinth as input
# and converts it into a picture. (Used in intermediate versions).
def mazeImageFunc(maze):
    # Create a new list for the image
    image_data = []

    # Adding maze data
    image_data.extend(maze)

    # Image Dimensions
    width = len(image_data[0])
    height = len(image_data)

    # Creating an Image
    image = Image.new("1", (width, height))  # "1" means binary mode

    # Filling an image with data from a list
    for y in range(height):
        for x in range(width):
            pixel_value = image_data[y][x]
            image.putpixel((x, y), pixel_value)

    # Saving an image
    image.save("maze.png")