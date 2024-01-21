import random

def generate_maze(width, height):
    # Создаем сетку лабиринта, где 0 - пустая клетка, 1 - стена
    maze = [[1] * (width // 2 * 2 + 1) for _ in range(height // 2 * 2 + 1)]

    # Создаем список для хранения посещенных клеток
    visited = set()

    # Функция для добавления пути между двумя клетками
    def connect_cells(cell1, cell2):
        x, y = cell1
        nx, ny = cell2
        maze[y][x] = 0
        maze[(y + ny) // 2][(x + nx) // 2] = 0

    # Начальная клетка
    start_cell = (random.randrange(width // 2) * 2 + 1, random.randrange(height // 2) * 2 + 1)
    visited.add(start_cell)
    stack = [start_cell]

    # Основной цикл
    while stack:
        x, y = stack[-1]
        neighbors = [(x + dx, y + dy) for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 < neighbor[0] < width and 0 < neighbor[1] < height and neighbor not in visited]

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            connect_cells((x, y), next_cell)
            visited.add(next_cell)
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

# Пример использования
width, height = 100, 100  # Указываем нечетные размеры для лучшего визуального представления лабиринта
maze = generate_maze(width, height)

# Вывод лабиринта
for row in maze:
    print("".join(["#" if cell == 1 else " " for cell in row]))
