import random
from algorithms.astar import astar


# ------------------------------------------------
# RED GHOST AI
# ------------------------------------------------
def move_ghost(
    maze,
    ghost_x,
    ghost_y,
    pacman_x,
    pacman_y,
    ghost_mode,
    frightened_mode
):

    # --------------------------------------------
    # FRIGHTENED MODE
    # --------------------------------------------
    if frightened_mode:

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        best_move = (ghost_x, ghost_y)

        max_distance = -1

        for dx, dy in directions:

            nx = ghost_x + dx
            ny = ghost_y + dy

            # Boundary + wall checking
            if (
                0 <= ny < len(maze)
                and
                0 <= nx < len(maze[0])
                and
                maze[ny][nx] != "#"
            ):

                distance = (
                    abs(nx - pacman_x)
                    +
                    abs(ny - pacman_y)
                )

                if distance > max_distance:

                    max_distance = distance

                    best_move = (nx, ny)

        return best_move

    # --------------------------------------------
    # CHASE MODE
    # --------------------------------------------
    if ghost_mode == "CHASE":

        # Aggressive pressure target
        target_x = pacman_x
        target_y = pacman_y
        path = astar(
            (ghost_x, ghost_y),
            (target_x, target_y),
            maze,
            ghost_x,
            ghost_y
        )

        if len(path) > 0:

            return path[0]

    # --------------------------------------------
    # SCATTER MODE
    # --------------------------------------------
    else:

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        random.shuffle(directions)

        for dx, dy in directions:

            nx = ghost_x + dx
            ny = ghost_y + dy

            # Boundary + wall checking
            if (
                0 <= ny < len(maze)
                and
                0 <= nx < len(maze[0])
                and
                maze[ny][nx] != "#"
            ):

                return (nx, ny)

    return (ghost_x, ghost_y)


# ------------------------------------------------
# BLUE GHOST RANDOM AI
# ------------------------------------------------
def move_blue_ghost(
    maze,
    blue_ghost_x,
    blue_ghost_y
):

    directions = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]

    random.shuffle(directions)
    # Sometimes stay still
    if random.random() < 0.25:
        return (blue_ghost_x, blue_ghost_y)

    for dx, dy in directions:

        nx = blue_ghost_x + dx
        ny = blue_ghost_y + dy

        # Boundary + wall checking
        if (
            0 <= ny < len(maze)
            and
            0 <= nx < len(maze[ny])
            and
            maze[ny][nx] != "#"
        ):

            return (nx, ny)

    return (blue_ghost_x, blue_ghost_y)
# ------------------------------------------------
# PINK GHOST PREDICTIVE AI
# ------------------------------------------------
def move_pink_ghost(
    maze,
    pink_ghost_x,
    pink_ghost_y,
    pacman_x,
    pacman_y,
    pacman_direction,
    frightened_mode
):

    # Predict future Pacman position
    target_x = pacman_x
    target_y = pacman_y

    prediction_distance = 1

    if pacman_direction == "RIGHT":
        target_x += prediction_distance

    elif pacman_direction == "LEFT":
        target_x -= prediction_distance

    elif pacman_direction == "UP":
        target_y -= prediction_distance

    elif pacman_direction == "DOWN":
        target_y += prediction_distance

    # Boundary safety
    target_x = max(
        0,
        min(target_x, len(maze[0]) - 1)
    )

    target_y = max(
        0,
        min(target_y, len(maze) - 1)
    )

    # Wall safety
    if maze[target_y][target_x] == "#":

        target_x = pacman_x
        target_y = pacman_y

    # A* toward predicted location
    path = astar(
        (pink_ghost_x, pink_ghost_y),
        (target_x, target_y),
        maze,
        pink_ghost_x,
        pink_ghost_y
    )

    if len(path) > 0:

        return path[0]

    return (pink_ghost_x, pink_ghost_y)