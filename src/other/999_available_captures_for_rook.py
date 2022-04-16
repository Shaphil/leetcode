def solve(board):
    rook = {'x': 0, 'y': 0}
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rook['x'] = i
                rook['y'] = j
    
    for i in range(8):
        pass
