import random

def play_game():
    choice = ['Rock', 'Paper', 'Scissor']
    computer_choice = random.choice(choice)
    print(computer_choice)
    for i in range(0, 30):
        print("#*#*") #Let's hide computers choice from the user!
    player_choice = choice[int(input("Please select your choice from below: "
                            "\n0: Rock"
                            "\n1: Paper"
                            "\n2: Scissor"
                            "\n"))]
    print(player_choice)
    if computer_choice == "Rock" and player_choice == "Scissor":
        # player_score += 1
        print(f"You won! CPU chose: {computer_choice} \n{player_choice} beats {computer_choice}")
        game_state()


        game_state()
    elif computer_choice == "Scissor" and player_choice == "Paper":
        # cpu_score += 1
        print(f"You lost! CPU chose: {computer_choice} \n{computer_choice} beats {player_choice}")
        game_state()

    elif player_choice == "Scissor" and computer_choice == "Paper":
        # player_score += 1
        print(f"You won! CPU chose: {computer_choice} \n{player_choice} beats {computer_choice}")
        game_state()

    elif player_choice == "Rock" and computer_choice == "Paper":
        # player_score += 1
        print(f"You lost! CPU chose: {computer_choice} \n{computer_choice} beats {player_choice}")
        game_state()
    elif player_choice == "Paper" and computer_choice == "Rock":
        # player_score += 1
        print(f"You won! CPU chose: {computer_choice} \n{player_choice} beats {computer_choice}")
        game_state()
    else:
        print(f"It's a tie! \n Your choice {player_choice} is same as CPU's choice of {computer_choice}")
        game_state()

def game_state():
    lets_play = input("Do you want to play Rock Paper Scissor again(Y/N)?: ")
    # player_name = input("Please enter your name: ")
    if lets_play == "Y":
        game_playing = True
    elif lets_play == "N":
        game_playing = False
        print("Thanks for playing!")
    while game_playing == True:
            return play_game()
            break

if __name__ == '__main__':
    play_game()



