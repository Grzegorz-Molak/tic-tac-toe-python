# write your code here
board_list = [[" "," "," "],[" "," "," "],[" "," "," "]]
1 
print("---------")
for x in range(3):
    print('|', board_list[x][0], board_list[x][1], board_list[x][2], '|')  
print("---------")

end = False
rounds = 0

while(end != True):
    while(1):
        coords = input("Enter the coordinates:").split()
        coord_x = ""
        coord_y = ""
        if(len(coords) == 2):
            coord_x = coords[0]
            coord_y = coords[1]
        else: 
            coord_x = "F"
            coord_y = "F"

        if not coord_x.isnumeric() or not coord_y.isnumeric():
            print("You should enter numbers!")
        else:
            coord_x = int(coord_x)
            coord_y = int(coord_y)
            if(1 <= coord_x <= 3 and 1 <= coord_y <= 3):
                if board_list[coord_x-1][coord_y-1] == 'X' or board_list[coord_x-1][coord_y-1] == 'O':
                    print("This cell is occupied! Choose another one!")
                else:
                    if rounds %2 == 0:
                        board_list[coord_x-1][coord_y-1] = 'X'
                    else:
                        board_list[coord_x-1][coord_y-1] = 'O'
                    break; 
                
            else:
                print("Coordinates should be from 1 to 3!")

    print("---------")
    for x in range(3):
        print('|', board_list[x][0], board_list[x][1], board_list[x][2], '|')  
    print("---------")

    rounds+= 1
    win_number = 0
    winner = 'X'
    for x in range(3):
        if board_list[x][0] == board_list[x][1] and board_list[x][1] == board_list[x][2] and board_list[x][0] != " ":
            #print("wygrana w rzedzie" + str(x))
            if board_list[x][0] == 'X':
                win_number+=1
                winner = 'X'
            else:
                win_number+=1
                winner = 'O'

    for y in range(3):
        if board_list[0][y] == board_list[1][y] and board_list[1][y] == board_list[2][y] and board_list[0][y] != " ":
            #print("wygrana w kolumnie" + str(y))
            if board_list[0][y] == 'X':
                win_number+=1
                winner = 'X'
            else:
                win_number+=1
                winner = 'O'

    if board_list[0][0] == board_list[1][1] == board_list[2][2] and board_list[0][0] != " ":
        #print("wygrana w skosie 1")
        if board_list[0][0] == 'X':
            win_number+=1
            winner = 'X'
        else:
            win_number+=1
            winner = 'O'

    if board_list[2][0] == board_list[1][1] == board_list[0][2] and board_list[2][0] != " ":
        #print("wygrana w skosie 2")
        if board_list[2][0] == 'X':
            win_number+=1
            winner = 'X'
        else:
            win_number+=1
            winner = 'O'
    if win_number == 0:
        if rounds == 9:
            print("Draw")
            end = True
    elif win_number == 1:
        print (winner + " wins")
        end = True