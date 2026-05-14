import pygame
import math
from utils.constants import *


# ------------------------------------------------
# Draw Pacman Style Ghost
# ------------------------------------------------
def draw_ghost(
    screen,
    x,
    y,
    color
):

    body_width = CELL_SIZE - 4
    body_height = CELL_SIZE - 4

    left = int(x + 2)
    top = int(y + 2)

    # ------------------------------------------------
    # Ghost Head
    # ------------------------------------------------
    pygame.draw.circle(
        screen,
        color,
        (
            left + body_width // 2,
            top + body_height // 3
        ),
        body_width // 2
    )

    # ------------------------------------------------
    # Ghost Body
    # ------------------------------------------------
    pygame.draw.rect(
        screen,
        color,
        (
            left,
            top + body_height // 3,
            body_width,
            body_height // 2
        )
    )

    # ------------------------------------------------
    # Ghost Legs
    # ------------------------------------------------
    leg_radius = body_width // 6

    for i in range(4):

        pygame.draw.circle(
            screen,
            color,
            (
                left + i * leg_radius * 2 + leg_radius,
                top + body_height - 2
            ),
            leg_radius
        )

    # ------------------------------------------------
    # Eyes
    # ------------------------------------------------
    eye_radius = 4

    # Left Eye
    pygame.draw.circle(
        screen,
        WHITE,
        (
            left + body_width // 3,
            top + body_height // 3
        ),
        eye_radius
    )

    # Right Eye
    pygame.draw.circle(
        screen,
        WHITE,
        (
            left + body_width * 2 // 3,
            top + body_height // 3
        ),
        eye_radius
    )

    # Pupils
    pygame.draw.circle(
        screen,
        BLUE,
        (
            left + body_width // 3,
            top + body_height // 3
        ),
        2
    )

    pygame.draw.circle(
        screen,
        BLUE,
        (
            left + body_width * 2 // 3,
            top + body_height // 3
        ),
        2
    )


# ------------------------------------------------
# Main Drawing Function
# ------------------------------------------------
def draw_game(
    screen,
    maze,
    pacman_px,
    pacman_py,
    ghost_px,
    ghost_py,
    score,
    lives,
    ghost_mode,
    font,
    mouth_angle,
    pacman_direction,
    blue_ghost_px,
    blue_ghost_py,
    frightened_mode,
    pink_ghost_px,
    pink_ghost_py
):

    # ------------------------------------------------
    # Background
    # ------------------------------------------------
    screen.fill(BLACK)

    # ------------------------------------------------
    # Top HUD Bar
    # ------------------------------------------------
    pygame.draw.rect(
        screen,
        (30, 30, 30),
        (0, 0, WIDTH, 45)
    )

    # ------------------------------------------------
    # Draw Maze
    # ------------------------------------------------
    for row in range(len(maze)):

        for col in range(len(maze[row])):

            x = col * CELL_SIZE
            y = row * CELL_SIZE + 50

            cell = maze[row][col]

            # ------------------------------------------------
            # Walls
            # ------------------------------------------------
            if cell == "#":

                pygame.draw.rect(
                    screen,
                    BLUE,
                    (
                        x,
                        y,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                )

            # ------------------------------------------------
            # Food Pellets
            # ------------------------------------------------
            elif cell == ".":

                pygame.draw.circle(
                    screen,
                    WHITE,
                    (
                        x + CELL_SIZE // 2,
                        y + CELL_SIZE // 2
                    ),
                    4
                )

            # ------------------------------------------------
            # Power Pellets
            # ------------------------------------------------
            elif cell == "O":

                pygame.draw.circle(
                    screen,
                    WHITE,
                    (
                        x + CELL_SIZE // 2,
                        y + CELL_SIZE // 2
                    ),
                    8
                )

    # ------------------------------------------------
    # Pacman Animation
    # ------------------------------------------------
    radius = CELL_SIZE // 2 - 2

    center_x = int(pacman_px + CELL_SIZE // 2)
    center_y = int(pacman_py + CELL_SIZE // 2 + 50)

    # ------------------------------------------------
    # Direction Angles
    # ------------------------------------------------
    if pacman_direction == "RIGHT":

        start_angle = math.radians(mouth_angle)
        end_angle = math.radians(360 - mouth_angle)

    elif pacman_direction == "LEFT":

        start_angle = math.radians(180 + mouth_angle)
        end_angle = math.radians(180 - mouth_angle)

    elif pacman_direction == "UP":

        start_angle = math.radians(270 + mouth_angle)
        end_angle = math.radians(270 - mouth_angle)

    else:

        start_angle = math.radians(90 + mouth_angle)
        end_angle = math.radians(90 - mouth_angle)

    # ------------------------------------------------
    # Pacman Body
    # ------------------------------------------------
    pygame.draw.circle(
        screen,
        YELLOW,
        (center_x, center_y),
        radius
    )

    # ------------------------------------------------
    # Pacman Mouth
    # ------------------------------------------------
    mouth_points = [

        (center_x, center_y),

        (
            center_x + radius * math.cos(start_angle),
            center_y - radius * math.sin(start_angle)
        ),

        (
            center_x + radius * math.cos(end_angle),
            center_y - radius * math.sin(end_angle)
        )
    ]

    pygame.draw.polygon(
        screen,
        BLACK,
        mouth_points
    )

    # ------------------------------------------------
    # Red Ghost
    # ------------------------------------------------
    draw_ghost(
        screen,
        ghost_px,
        ghost_py + 50,
        (50, 50, 255) if frightened_mode else RED
    )

    # ------------------------------------------------
    # Blue Ghost
    # ------------------------------------------------
    draw_ghost(
        screen,
        blue_ghost_px,
        blue_ghost_py + 50,
        (0, 255, 255)
    )

    # ------------------------------------------------
    # Pink Ghost
    # ------------------------------------------------
    draw_ghost(
        screen,
        pink_ghost_px,
        pink_ghost_py + 50,
        (255, 105, 180)
    )

    # ------------------------------------------------
    # Score UI
    # ------------------------------------------------
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, 10)
    )

    # ------------------------------------------------
    # Lives UI
    # ------------------------------------------------
    lives_text = font.render(
        f"Lives: {lives}",
        True,
        WHITE
    )

    screen.blit(
        lives_text,
        (250, 10)
    )