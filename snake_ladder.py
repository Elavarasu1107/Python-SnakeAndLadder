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
    winning_position = 100
    no_of_times_dice_rolled = 0

    while player_position < winning_position:
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
        if player_position > winning_position:
            player_position -= dice_value
        no_of_times_dice_rolled += 1
        print("Player Position: ", player_position)

    print("Number of times dice rolled: ", no_of_times_dice_rolled)
    print("Player Position: ", player_position)


if __name__ == '__main__':
    snake_ladder()
