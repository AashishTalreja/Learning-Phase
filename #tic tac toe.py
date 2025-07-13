#tic tac toe
board=[""for i in range(9)] #used to create empty1 spaces from 0 to 8th
def table():
    row1="| {} |  | {} |  | {} |".format(board[0],board[1],board[2])  
    row2="| {} |  | {} |  | {} |".format(board[3],board[4],board[5])
    row3="| {} |  | {} |  | {} |".format(board[6],board[7],board[8])
    print()  #used to create empty line so that it looks organised
    print(row1)
    print(row2)
    print(row3)
    print()


def move(icon):
    if icon=="X":
        num=1
    elif icon=="O":
        num=2
    else:
        print("invalid input")
    print("your turn player {}".format(num))
    choice=int(input("enter your choice 1-9:\n").strip())
    if board[choice-1]=="":
        board[choice-1]=icon
    else:
        print()
        print("space is occupied and creampied")
        move(icon)



def vict(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or \
    (board[3]==icon and board[4]==icon and board[5]==icon) or \
    (board[6]==icon and board[7]==icon and board[8]==icon) or \
    (board[0]==icon and board[4]==icon and board[8]==icon) or \
    (board[2]==icon and board[4]==icon and board[6]==icon) or \
    (board[0]==icon and board[3]==icon and board[6]==icon) or \
    (board[1]==icon and board[4]==icon and board[7]==icon) or \
    (board[2]==icon and board[5]==icon and board[8]==icon):
        return True
    else:
        return False




def draw():
    if "" not in board:
        return True
    else:
        return False





while True:
    table()
    move("X")
    table()
    if vict("X"):
        print("congrats X for winning the game")
        break       
    elif draw():
        print("the game is draw")
        break
    table()
    move("O")
    if vict("O"):
        table()
        print("congrats O for winning the game")
        break
    elif draw():
        print("the game is draw")
        break