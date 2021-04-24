import random
game_playing = False
player_score = 0
cpu_score = 0
choice = ['Rock', 'Paper', 'Scissor']
computer_choice = random.choice(choice)
pick = choice[int(input("Please select your choice from below: "
                        "\n0: Rock"
                        "\n1: Paper"
                        "\n2: Scissor"
                        "\n"))]
