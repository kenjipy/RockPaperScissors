import random   
game_list =['rock' ,'paper', 'scissors']
comuter = c = 0
command = p = 0
print("score: Computer" + str(c) + "player" + str(p))
#the loop
run = True
while run:
    computer_choce = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")
    if command == computer_choice: 
        print("Tie")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("player won!")
            p += 1
        else:
            print("Computer won!")
            c += 1
        elif command == 'Paper':
            if command == 'Rock':
                print('Player won!')
                p += 1
            else:
             print("computer won!")
            c += 1

                elif command == 'Scissors':
            if command == 'Paper':
                print('Player won!')
                p += 1
            else:
             print("computer won!")
            c += 1
            
            elif command == 'Quit' :
                break
            else:
            
            
                print("Wrong command!")
            print("player " + command)
            print("computer " + computer_choce)
            print("")
            print("score: computer " + str(c) + "Player" + str(p))
            print("")
