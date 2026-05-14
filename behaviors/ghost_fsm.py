def update_ghost_mode(
    ghost_mode,
    mode_timer
):

    mode_timer += 1

    if mode_timer >= 25:

        mode_timer = 0

        if ghost_mode == "CHASE":
            ghost_mode = "SCATTER"

        else:
            ghost_mode = "CHASE"

    return ghost_mode, mode_timer