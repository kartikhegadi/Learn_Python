the_board={
    'top-l':' ' ,'top-m':'','top-r':'',
    'mid-l':' ' ,'mid-m':'','mid-r':'',
    'low-l':' ' ,'low-m':'','low-r':''
}
def print_board(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
turn='x'
for i in range(9):
    print_board(the_board)
    print("turn for"+turn+'.Move on which space')
    move=input()
    the_board[move]=turn
    if turn=='x':
        turn='0'
    else:
        turn='x'
print_board(the_board)
