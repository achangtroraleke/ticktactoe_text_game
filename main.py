board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]


def display(gameboard):
    for x in gameboard:
        print(x)



def check_winner(board):
       for n in board:

              # check each column for the value and sees if they match.
              if n[0] == n[1] and n[0] == n[2]:
                     print(f'Winning is {str(n[1])}')
                     return True

              elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                     winner = str(board[1][1])
                     print(f'Winner is {winner}')
                     return True
              elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
                     winner = str(board[1][1])
                     print(f'Winner is {winner}')
                     return True
              elif board[0][0] == board[1][1] and board[1][1]== board[2][0]:
                     winner = str(board[1][1])
                     print(f'Winner is {winner}')
                     return True

              else:
                     for i in range(0, len(n)):
                            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                                   winner = str(board[0][i])
                                   print(f'Winner is {winner}')
                                   return True

                     return False
is_winner = False
              #checks each row if there is a winner.




print('X goes first')
x_turn = True



while not is_winner:


       if x_turn:
              display(board)
              x_move = input("X player where would you like to go?\n")
              if int(x_move) < 1 or int(x_move) > 9:
                     print('That choice is not valid')
              elif int(x_move) == 1 and board[0][0] != 'o':
                     board[0][0] = 'x'
                     x_turn = False

              elif int(x_move) == 2 and board[0][1] != 'o':
                     board[0][1] = 'x'
                     x_turn = False

              elif int(x_move) == 3 and board[0][2] != 'o':
                     board[0][2] = 'x'
                     x_turn = False

              elif int(x_move) == 4 and board[1][0] != 'o':
                     board[1][0] = 'x'
                     x_turn = False

              elif int(x_move) == 5 and board[1][1] != 'o':
                     board[1][1] = 'x'
                     x_turn = False

              elif int(x_move) == 6 and board[1][2] != 'o':
                     board[1][2] = 'x'
                     x_turn = False

              elif int(x_move) == 7 and board[2][0] != 'o':
                     board[2][0] = 'x'
                     x_turn = False

              elif int(x_move) == 8 and board[2][1] != 'o':
                     board[2][1] = 'x'
                     x_turn = False
              elif int(x_move) == 9 and board[2][2] != 'o':
                     board[2][2] = 'x'
                     x_turn = False
              else:
                     print('That spot is already taken.')


       if not x_turn:
              display(board)
              o_move = input("O player where would you like to go?\n")

              if int(o_move) < 1 or int(o_move) > 9:
                     print('That choice is not valid')
              elif int(o_move) == 1 and board[0][0] != 'x':
                     board[0][0] = 'o'
                     x_turn = True

              elif int(o_move) == 2 and board[0][1] != 'x':
                     board[0][1] = 'o'
                     x_turn = True

              elif int(o_move) == 3 and board[0][2] != 'x':
                     board[0][2] = 'o'
                     x_turn = True

              elif int(o_move) == 4 and board[1][0] != 'x':
                     board[1][0] = 'o'
                     x_turn = True

              elif int(o_move) == 5 and board[1][1] != 'x':
                     board[1][1] = 'o'
                     x_turn = True

              elif int(o_move) == 6 and board[1][2] != 'x':
                     board[1][2] = 'o'
                     x_turn = True

              elif int(o_move) == 7 and board[2][0] != 'x':
                     board[2][0] = 'o'
                     x_turn = True

              elif int(o_move) == 8 and board[2][1] != 'x':
                     board[2][1] = 'o'
                     x_turn = True
              elif int(o_move) == 9 and board[2][2] != 'x':
                     board[2][2] = 'o'
                     x_turn = True
              else:

                     print("That spot is already taken.")

       is_winner = check_winner(board)

