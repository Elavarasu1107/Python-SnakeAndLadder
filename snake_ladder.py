import random


def snake_ladder():
    """
    This function is a simple snake and ladder game.
    If a player reaches the exact position of 100, printed as player won the game
    :return: None
    """
    player_position = 0
    dice_value = random.randint(1, 6)
    print("Player Position: ", player_position)
    print("Dice Value: ", dice_value)


if __name__ == '__main__':
    snake_ladder()
