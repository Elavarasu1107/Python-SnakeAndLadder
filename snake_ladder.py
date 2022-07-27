import random


def snake_ladder():
    """
    This function is a simple snake and ladder game consist of two players.
    If a player reaches the exact position of 100, printed as player won the game
    :return: None
    """
    player1_position = 0
    player2_position = 0
    is_no_play = 0
    is_snake = 1
    is_ladder = 2
    winning_position = 100
    player_turn = 1
    no_of_times_dice_rolled = 0
    player1_dice_rolled = 0
    player2_dice_rolled = 0

    while player1_position < winning_position and player2_position < winning_position:
        if player_turn == 1:
            player_turn += 1
            player_option = random.randint(0, 2)
            dice_value = random.randint(1, 6)
            if player_option == is_ladder:
                player1_position += dice_value
                player_turn -= 1
            elif player_option == is_snake:
                player1_position -= dice_value
                if player1_position < 0:
                    player1_position = 0
            else:
                player1_position += is_no_play
            if player1_position > winning_position:
                player1_position -= dice_value
            player1_dice_rolled += 1
        else:
            player_turn -= 1
            player_option = random.randint(0, 2)
            dice_value = random.randint(1, 6)
            if player_option == is_ladder:
                player2_position += dice_value
                player_turn += 1
            elif player_option == is_snake:
                player2_position -= dice_value
                if player2_position < 0:
                    player2_position = 0
            else:
                player2_position += is_no_play
            if player2_position > winning_position:
                player2_position -= dice_value
            player2_dice_rolled += 1

        no_of_times_dice_rolled += 1

    print("Number of times dice rolled: ", no_of_times_dice_rolled)
    print("Player one Dice Rolled: ", player1_dice_rolled)
    print("Player two Dice Rolled: ", player2_dice_rolled)
    print("Player One Position: ", player1_position)
    print("Player Two Position: ", player2_position)

    if player1_position > player2_position:
        print("Player One Won the Game")
    else:
        print("Player Two Won the Game")


if __name__ == '__main__':
    snake_ladder()
