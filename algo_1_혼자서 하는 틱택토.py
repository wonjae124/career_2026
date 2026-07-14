def solution(board):
    oCnt = 0
    xCnt = 0
    oBingoCnt = 0
    xBingoCnt = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                oCnt += 1
            elif board[i][j] == 'X':
                xCnt += 1

    if oCnt < xCnt or oCnt - xCnt > 1:
        return 0

    for k in range(3):
        if board[k][0] == board[k][1] == board[k][2] == 'O':
            oBingoCnt += 1
        if board[k][0] == board[k][1] == board[k][2] == 'X':
            xBingoCnt += 1
        if board[0][k] == board[1][k] == board[2][k] == 'O':
            oBingoCnt += 1
        if board[0][k] == board[1][k] == board[2][k] == 'X':
            xBingoCnt += 1

    if board[0][0] == board[1][1] == board[2][2] == 'O':
        oBingoCnt += 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        oBingoCnt += 1
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        xBingoCnt += 1
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        xBingoCnt += 1

    if oBingoCnt > 0 and xBingoCnt > 0:   # 둘 다 이긴 상황은 불가능
        return 0
    if oBingoCnt > 0 and oCnt != xCnt + 1:  # O 승리면 마지막 수가 O → O가 하나 많아야 함
        return 0
    if xBingoCnt > 0 and oCnt != xCnt:      # X 승리면 마지막 수가 X → 개수가 같아야 함
        return 0

    return 1