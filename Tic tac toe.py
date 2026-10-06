# Tic Tac Toe Game

# board for game
board=[" " for _ in range(9)]

def display_board():
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("--+--+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+--+--")
    print(board[6],"|",board[7],"|",board[8])
    print()
# for winning patterns
def checking_winner(player):
    winPatterns=[(0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6)]
    
    for a,b,c in winPatterns:
        if(board[a]==player and board[b]==player and board[c]==player):
            return True
        
    return False
            
# for no space
def board_full():
    return " " not in board    

# game function
def play_game():
    current_player="X"
    while True:
        display_board()
        position=int(input("choose your position (1-9): "))-1
        
        if position < 0 or position > 8:
            print("Invalid position")
            continue
        
        if board[position] != " ":
            print("The position is already taken!")
            continue
        
        board[position]=current_player
        
        # check winner
        if checking_winner(current_player):
            display_board()
            print("Player",current_player,"wins!")
            break
        
        if board_full():
            display_board()
            print("It's a draw ")
            break
        # change player

        if current_player=="X":
            current_player="O"
        else:
            current_player="X"
play_game()
