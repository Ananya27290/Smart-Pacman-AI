import pygame
import sys

from utils.constants import *
from environment.maze import maze

from agents.ghost_agent import (
    move_ghost,
    move_blue_ghost,
    move_pink_ghost
)

from behaviors.ghost_fsm import update_ghost_mode
from rendering.draw import draw_game

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Pacman AI")

font = pygame.font.SysFont(None, 32)
title_font = pygame.font.SysFont(None, 72)

# ------------------------------------------------
# MENU STATE
# ------------------------------------------------
game_started = False

# ------------------------------------------------
# Pacman Position
# ------------------------------------------------
pacman_x = 1
pacman_y = 1

pacman_px = pacman_x * CELL_SIZE
pacman_py = pacman_y * CELL_SIZE

# ------------------------------------------------
# Ghost Positions
# ------------------------------------------------
ghost_x = 14
ghost_y = 3

blue_ghost_x = 22
blue_ghost_y = 10

pink_ghost_x = 4
pink_ghost_y = 15

ghost_px = ghost_x * CELL_SIZE
ghost_py = ghost_y * CELL_SIZE

blue_ghost_px = blue_ghost_x * CELL_SIZE
blue_ghost_py = blue_ghost_y * CELL_SIZE

pink_ghost_px = pink_ghost_x * CELL_SIZE
pink_ghost_py = pink_ghost_y * CELL_SIZE

# ------------------------------------------------
# Game Variables
# ------------------------------------------------
score = 0
lives = 3

game_over = False
game_won = False

MOVE_SPEED = 4

mouth_angle = 0
mouth_opening = True

pacman_direction = "RIGHT"

ghost_timer = 0
ghost_mode = "SCATTER"

frightened_timer = 0
frightened_mode = False

mode_timer = 0

running = True

# ------------------------------------------------
# Main Loop
# ------------------------------------------------
while running:

    # ------------------------------------------------
    # MENU SCREEN
    # ------------------------------------------------
    if not game_started:

        screen.fill(BLACK)

        title_text = title_font.render(
            "SMART PACMAN AI",
            True,
            YELLOW
        )

        start_text = font.render(
            "Press ENTER to Start",
            True,
            WHITE
        )

        exit_text = font.render(
            "Press ESC to Exit",
            True,
            WHITE
        )

        controls_text = font.render(
            "Use Arrow Keys to Move",
            True,
            (180, 180, 180)
        )

        screen.blit(title_text, (160, 180))
        screen.blit(start_text, (280, 300))
        screen.blit(exit_text, (300, 350))
        screen.blit(controls_text, (250, 420))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    game_started = True

                elif event.key == pygame.K_ESCAPE:
                    running = False

        continue

    # ------------------------------------------------
    # EVENT HANDLING
    # ------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if (
            not game_over
            and
            not game_won
            and
            event.type == pygame.KEYDOWN
        ):

            new_x = pacman_x
            new_y = pacman_y

            # LEFT
            if event.key == pygame.K_LEFT:

                pacman_direction = "LEFT"
                new_x -= 1

            # RIGHT
            elif event.key == pygame.K_RIGHT:

                pacman_direction = "RIGHT"
                new_x += 1

            # UP
            elif event.key == pygame.K_UP:

                pacman_direction = "UP"
                new_y -= 1

            # DOWN
            elif event.key == pygame.K_DOWN:

                pacman_direction = "DOWN"
                new_y += 1

            # WALL COLLISION
            if (
                0 <= new_y < len(maze)
                and
                0 <= new_x < len(maze[new_y])
                and
                maze[new_y][new_x] != "#"
            ):

                pacman_x = new_x
                pacman_y = new_y

                # FOOD
                if maze[pacman_y][pacman_x] == ".":

                    maze[pacman_y][pacman_x] = " "
                    score += 1

                # POWER PELLET
                elif maze[pacman_y][pacman_x] == "O":

                    maze[pacman_y][pacman_x] = " "

                    score += 10

                    frightened_mode = True
                    frightened_timer = 180

    # ------------------------------------------------
    # CHECK WIN
    # ------------------------------------------------
    if not game_over:

        food_remaining = False

        for row in maze:

            if "." in row or "O" in row:
                food_remaining = True

        if not food_remaining:
            game_won = True

    # ------------------------------------------------
    # GHOST FSM
    # ------------------------------------------------
    if not game_over and not game_won:

        ghost_mode, mode_timer = update_ghost_mode(
            ghost_mode,
            mode_timer
        )

    # ------------------------------------------------
    # FRIGHTENED TIMER
    # ------------------------------------------------
    if frightened_mode:

        frightened_timer -= 1

        if frightened_timer <= 0:
            frightened_mode = False

    # ------------------------------------------------
    # GHOST MOVEMENT
    # ------------------------------------------------
    ghost_timer += 1

    ghost_speed = max(5, 12 - score // 5)

    if ghost_timer >= ghost_speed:

        ghost_timer = 0

        if not game_over and not game_won:

            ghost_x, ghost_y = move_ghost(
                maze,
                ghost_x,
                ghost_y,
                pacman_x,
                pacman_y,
                ghost_mode,
                frightened_mode
            )

            blue_ghost_x, blue_ghost_y = move_blue_ghost(
                maze,
                blue_ghost_x,
                blue_ghost_y
            )

            pink_ghost_x, pink_ghost_y = move_pink_ghost(
                maze,
                pink_ghost_x,
                pink_ghost_y,
                pacman_x,
                pacman_y,
                pacman_direction,
                frightened_mode
            )

    # ------------------------------------------------
    # COLLISION DETECTION
    # ------------------------------------------------
    collision = (

        (
            ghost_x == pacman_x
            and
            ghost_y == pacman_y
        )

        or

        (
            blue_ghost_x == pacman_x
            and
            blue_ghost_y == pacman_y
        )

        or

        (
            pink_ghost_x == pacman_x
            and
            pink_ghost_y == pacman_y
        )
    )

    if collision and not game_over:

        lives -= 1

        pacman_x = 1
        pacman_y = 1

        pacman_px = pacman_x * CELL_SIZE
        pacman_py = pacman_y * CELL_SIZE

        ghost_x = 14
        ghost_y = 3

        blue_ghost_x = 22
        blue_ghost_y = 10

        pink_ghost_x = 4
        pink_ghost_y = 15

        ghost_px = ghost_x * CELL_SIZE
        ghost_py = ghost_y * CELL_SIZE

        blue_ghost_px = blue_ghost_x * CELL_SIZE
        blue_ghost_py = blue_ghost_y * CELL_SIZE

        pink_ghost_px = pink_ghost_x * CELL_SIZE
        pink_ghost_py = pink_ghost_y * CELL_SIZE

        pygame.time.delay(500)

        if lives <= 0:
            game_over = True

    # ------------------------------------------------
    # SMOOTH MOVEMENT
    # ------------------------------------------------
    target_px = pacman_x * CELL_SIZE
    target_py = pacman_y * CELL_SIZE

    if pacman_px < target_px:
        pacman_px += MOVE_SPEED

    if pacman_px > target_px:
        pacman_px -= MOVE_SPEED

    if pacman_py < target_py:
        pacman_py += MOVE_SPEED

    if pacman_py > target_py:
        pacman_py -= MOVE_SPEED

    # RED GHOST
    ghost_target_px = ghost_x * CELL_SIZE
    ghost_target_py = ghost_y * CELL_SIZE

    if ghost_px < ghost_target_px:
        ghost_px += MOVE_SPEED

    if ghost_px > ghost_target_px:
        ghost_px -= MOVE_SPEED

    if ghost_py < ghost_target_py:
        ghost_py += MOVE_SPEED

    if ghost_py > ghost_target_py:
        ghost_py -= MOVE_SPEED

    # BLUE GHOST
    blue_target_px = blue_ghost_x * CELL_SIZE
    blue_target_py = blue_ghost_y * CELL_SIZE

    if blue_ghost_px < blue_target_px:
        blue_ghost_px += MOVE_SPEED

    if blue_ghost_px > blue_target_px:
        blue_ghost_px -= MOVE_SPEED

    if blue_ghost_py < blue_target_py:
        blue_ghost_py += MOVE_SPEED

    if blue_ghost_py > blue_target_py:
        blue_ghost_py -= MOVE_SPEED

    # PINK GHOST
    pink_target_px = pink_ghost_x * CELL_SIZE
    pink_target_py = pink_ghost_y * CELL_SIZE

    if pink_ghost_px < pink_target_px:
        pink_ghost_px += MOVE_SPEED

    if pink_ghost_px > pink_target_px:
        pink_ghost_px -= MOVE_SPEED

    if pink_ghost_py < pink_target_py:
        pink_ghost_py += MOVE_SPEED

    if pink_ghost_py > pink_target_py:
        pink_ghost_py -= MOVE_SPEED

    # ------------------------------------------------
    # PACMAN MOUTH ANIMATION
    # ------------------------------------------------
    if mouth_opening:

        mouth_angle += 2

        if mouth_angle >= 30:
            mouth_opening = False

    else:

        mouth_angle -= 2

        if mouth_angle <= 5:
            mouth_opening = True

    # ------------------------------------------------
    # DRAW GAME
    # ------------------------------------------------
    draw_game(
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
    )

    # ------------------------------------------------
    # GAME OVER
    # ------------------------------------------------
    if game_over:

        text = font.render(
            "GAME OVER!",
            True,
            RED
        )

        screen.blit(text, (300, 300))

    # ------------------------------------------------
    # YOU WIN
    # ------------------------------------------------
    elif game_won:

        text = font.render(
            "YOU WIN!",
            True,
            GREEN
        )

        screen.blit(text, (320, 300))

    pygame.display.update()

    pygame.time.delay(16)

pygame.quit()
sys.exit()