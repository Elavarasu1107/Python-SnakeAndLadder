import random


def snake_ladder():
    """
    This function is a simple snake and ladder game.
    If a player reaches the exact position of 100, printed as player won the game
    :return: None
    """
    player_position = 0
    is_no_play = 0
    is_snake = 1
    is_ladder = 2
    player_option = random.randint(0, 2)
    dice_value = random.randint(1, 6)

    if player_option == is_ladder:
        player_position += dice_value
    elif player_option == is_snake:
        player_position -= dice_value
        if player_position < 0:
            player_position = 0
    else:
        player_position += is_no_play

    print("Player Position: ", player_position)


if __name__ == '__main__':
    snake_ladder()
