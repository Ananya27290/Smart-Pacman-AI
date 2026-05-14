from algorithms.astar import astar

# Find nearest food
def find_food(maze, pacman_x, pacman_y):

    nearest_food = None
    shortest_distance = 9999

    for y in range(len(maze)):
        for x in range(len(maze[y])):

            if maze[y][x] == ".":

                distance = abs(x - pacman_x) + abs(y - pacman_y)

                if distance < shortest_distance:

                    shortest_distance = distance
                    nearest_food = (x, y)

    return nearest_food


# Pacman AI movement
def move_pacman(
    maze,
    pacman_x,
    pacman_y,
    ghost_x,
    ghost_y
):

    goal = find_food(
        maze,
        pacman_x,
        pacman_y
    )

    if goal:

        path = astar(
            (pacman_x, pacman_y),
            goal,
            maze,
            ghost_x,
            ghost_y
        )

        if len(path) > 0:

            return path[0]

    return (pacman_x, pacman_y)