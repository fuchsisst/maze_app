import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_RETURN
from functions.add_border_func import addBorderFunc
from functions.convert_to_binary_func import convertToBinaryFunc
from functions.maze_generation_func import mazeGenerationFunc

# Doesn't solve the problem well, needs to be replaced
def add_random_passages(maze):
    height = len(maze)
    width = len(maze[0])

    def is_valid_position(row, col):
        return 0 <= row < height and 0 <= col < width

    def has_adjacent_wall(row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_position(new_row, new_col) and maze[new_row][new_col] == 0:
                return True
        return False

    modified_maze = [row[:] for row in maze]

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if maze[row][col] == 0 and not has_adjacent_wall(row, col):
                if random.choice([True, False]):
                    modified_maze[row][col] = 1

    for col in range(1, width - 1):
        for row in range(1, height - 1):
            if maze[row][col] == 0 and not has_adjacent_wall(row, col):
                if random.choice([True, False]):
                    modified_maze[row][col] = 1

    return modified_maze


TARGET = 3
PATH = 1
# Creating a congratulations window
def show_congratulations_screen():
   
    congratulations_screen = pygame.display.set_mode((567, 567))
    pygame.display.set_caption("Maze")

    font = pygame.font.Font(None, 24)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        pygame.draw.rect(congratulations_screen, (173, 216, 230), (0, 0, 567, 567))
        text = font.render("Congratulations, you have completed the maze!", True, (0, 0, 0))
        congratulations_screen.blit(text, (100, 50))

        continue_text = font.render("Press \'Enter' to continue the game", True, (0, 0, 0))
        congratulations_screen.blit(continue_text, (150, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    running = False
                    run_maze_game()

    pygame.quit()
    
def run_maze_game():
    # Definition of a labyrinth
    length = 63
    width = 63
    maze = mazeGenerationFunc(length, width, [])
    
    
    addBorderFunc(maze, width)
    convertToBinaryFunc(maze)
    mazeFinish = add_random_passages(maze)
    # Finding passages in the maze (elements with value 1)
    path_positions = [(row, col) for row in range(len(mazeFinish)) for col in range(len(mazeFinish[0])) if mazeFinish[row][col] == PATH]

    # Select a random pass and set the value to 3
    if path_positions:
        target_position = random.choice(path_positions)
        mazeFinish[target_position[0]][target_position[1]] = TARGET
    else:
        print("The labyrinth does not contain passages.")
        
    # Initializing Pygame
    pygame.init()
    cell_size = 9
    width = len(mazeFinish[0])
    height = len(mazeFinish)
    screen_size = (width * cell_size, height * cell_size)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Maze")

    # Create a player
    player_image = pygame.Surface((cell_size, cell_size))
    player_image.fill((255, 0, 0))
    player_pos = [1, 1]
    direction = [0, 0]

    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = [0, -1]
                elif event.key == K_DOWN:
                    direction = [0, 1]
                elif event.key == K_LEFT:
                    direction = [-1, 0]
                elif event.key == K_RIGHT:
                    direction = [1, 0]

        new_pos = [player_pos[0] + direction[0], player_pos[1] + direction[1]]

        if 0 <= new_pos[0] < width and 0 <= new_pos[1] < height:
            cell_value = mazeFinish[new_pos[1]][new_pos[0]]
            if cell_value == 1 :
                player_pos = new_pos
            elif cell_value == 2:
                player_pos = new_pos
                pygame.time.delay(200)
                possible_directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for direction in possible_directions:
                    next_pos = [player_pos[0] + direction[0], player_pos[1] + direction[1]]
                    if 0 <= next_pos[0] < width and 0 <= next_pos[1] < height:
                        if mazeFinish[next_pos[1]][next_pos[0]] == 1:
                            player_pos = next_pos
                            break
            elif cell_value == 3: 
                player_pos = new_pos # If the player reaches the goal
                show_congratulations_screen()

        screen.fill((255, 255, 255))
        for y in range(height):
            for x in range(width):
                if mazeFinish[y][x] == 0:
                    # Walls color
                    pygame.draw.rect(screen, (60, 106, 132), (x * cell_size, y * cell_size, cell_size, cell_size))
                elif mazeFinish[y][x] == 1:
                    # Roads color
                    pygame.draw.rect(screen, (211, 240, 254), (x * cell_size, y * cell_size, cell_size, cell_size))
                elif mazeFinish[y][x] == TARGET:
                    pygame.draw.rect(screen, (0, 255, 0), (x * cell_size, y * cell_size, cell_size, cell_size))
            screen.blit(player_image, (player_pos[0] * cell_size, player_pos[1] * cell_size))
                

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


# Main code
pygame.init()
screen_width, screen_height = 567, 567
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Maze")
pygame.display.set_icon(pygame.image.load("C:/Users/vital/Maze_Python/assets/images/bullfinch_in_winter_best_pixel.jpeg"))

background_image = pygame.image.load("C:/Users/vital/Maze_Python/assets/images/snow_forest_best_pixel_art_neo.jpeg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

pygame.mixer.music.load("C:/Users/vital/Maze_Python/assets/musics/sinnesloschen-beam-117362.mp3")
pygame.mixer.music.play(-1)  # -1 means endless playback

font = pygame.font.Font(None, 24)

start_button_rect = pygame.Rect(screen_width // 2 - 70, 200, 140, 35)
exit_button_rect = pygame.Rect(screen_width // 2 - 70, 250, 140, 35)

current_screen = "main"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "main":
                if start_button_rect.collidepoint(event.pos):
                    current_screen = "maze"
                    run_maze_game()
                    show_congratulations_screen()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    start_button_color = (0, 255, 255) if start_button_rect.collidepoint((mouse_x, mouse_y)) else (0, 200, 200)
    exit_button_color = (0, 255, 255) if exit_button_rect.collidepoint((mouse_x, mouse_y)) else (0, 200, 200)

    screen.blit(background_image, (0, 0))
    
    pygame.draw.rect(screen, start_button_color, start_button_rect)
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)

    start_text = font.render("Start", True, (30, 30, 30))
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    screen.blit(start_text, start_text_rect)

    exit_text = font.render("Exit", True, (30, 30, 30))
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
    screen.blit(exit_text, exit_text_rect)

    pygame.display.flip()

