import heapq

# Heuristic Function
def heuristic(a, b):

    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)


# Danger detection
def is_dangerous(x, y, ghost_x, ghost_y):

    distance = abs(x - ghost_x) + abs(y - ghost_y)

    return distance <= 1


# A* Algorithm
def astar(start, goal, maze, ghost_x, ghost_y):

    open_set = []

    heapq.heappush(open_set, (0, start, []))

    visited = set()

    while open_set:

        cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        x, y = current

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            neighbor = (nx, ny)

            if neighbor in visited:
                continue

            if maze[ny][nx] == "#":
                continue

            if not is_dangerous(nx, ny, ghost_x, ghost_y):
                g = len(path) + 1
            else:
                g = len(path) + 5

            h = heuristic(neighbor, goal)

            f = g + h

            heapq.heappush(
                open_set,
                (
                    f,
                    neighbor,
                    path + [neighbor]
                )
            )

    return []