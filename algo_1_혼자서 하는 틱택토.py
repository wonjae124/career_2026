'''
접근법
- 선공 O, 후공 X
- 승리 조건 : O가 연달아 3개 그려지면 O, X가 연달아 3개이면 X가 승
- 주어진 board 배열을 보고, 이게 가능한 게임 플레이이면 1, 불가하면 0
    불가 상황
        - 1. 순서를 어긴 상황  
            - 판단 기준 ?
        - 2. 이미 누군가 승리한 상황
            - 판단 기준 ?
유의점
- O든 X든 채워진 칸이 9개이면 무승부로 종료

푸는 법
- 이걸 어떻게 풀어야 하지?
- O를 찾고 그 다음 X를 찾고 이후 O를 찾고 다시 X를 찾는 식으로 해야 하는거겠네?
- 찍으면서 빙고가 완성된 이후에, O나 X가 보이면 0이고 아니면 1이다.
- 빙고의 상태를 어떻게 기억하지? 움직이는 경우를 어떻게 지정할지 잘 모르겠음.
  세로, 가로, 대각선 3가지 케이스가 있단 말이다....
- .이 나오면 그 쪽 방향은 빙고 끝난거므로 카운트 끝내고, 만약 같은 값이 나오면 빙고 카운트 계속한다.
- 방문한 케이스를 저장하는 배열은 만들어둬야 하나?? 잘 모르겠다.
- 누가 다음에 O를 넣는지 확인 필요

문제의 본질
    1) 누가 이기든 말든 상관없음. 그저 제대로 진행된 케이스인가를 확인하는 경우
    2) 그냥 빙고가 2개 이상인 경우가 있으면 실패한걸로 보기
    
엣지 케이스
    1) O가 선공인데 X가 선공을 한 경우는 0 출력
    2) 모두 점일 경우에는 1 출력
    3) 게임이 끝나지 않는 경우에 정상여부 판단
    
풀기
[1차] = 48.1점
- 1) board를 전부 돌면서, O의 개수와 X의 개수를 센다
    (O의 개수 <  X의 개수) or (0의 개수 - X의 개수 > 1)
        => 실패(0) 반환
    0의 개수 >= X의 개수 
        => 성공(1) 반환
    
- 2) board를 총 16번 빙고를 확인한다. 1/2/3행과 1/2/3열이 왼쪽/오른쪽 대각선이 전부 O인지, 
     이후에 전부 X인지. 각 개수를 따로따로 구한다.
    |O 빙고 개수 - X 빙고 개수| <= 1 
        => 성공(1) 반환 

[2차] 100점
- 빙고의 개수가 아니라, 빙고의 여부로 따짐.
배경:
    개수로 푸니 빙고가 아예 없는 경우인 입출력 예시 1번, 3, 4번에서 에러 발생함. 
    왜냐하면 빙고가 없는거지 0개가 아님.
    애초에 고려하면 안됨. 

문제 유형
- 구현

알고리즘
- 모름

시간 복잡도
풀이 시간 : 26.07.14, 5시간 소요
'''
def solution(board):
    '''
        board를 읽는걸 두 번 하면 되겠다.
        1) 파이썬 배열 읽기 어케 하더라
        2) 변수 선언 뭐 하려고 했지?
    '''
    answer = -1

    oCnt = 0
    xCnt = 0
    dotCnt = 0
    oBingoCnt = 0
    xBingoCnt = 0;

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                oCnt += 1
            elif board[i][j] == 'X':
                xCnt += 1
            else:
                dotCnt += 1

    if dotCnt == 9:
        return 1

    if oCnt < xCnt or oCnt - xCnt > 1:
        answer = 0
        print('aaa')
        return answer
    # else:
    #     print('ggg')
    #     answer = 1

    for k in range(3):
        # 행( -> 방향) 비교
        if board[k][0] == board[k][1] == board[k][2] == 'O':
            oBingoCnt += 1
        if board[k][0] == board[k][1] == board[k][2] == 'X':
            xBingoCnt += 1
            # 열( 아래 방향) 비교
        if board[0][k] == board[1][k] == board[2][k] == 'O':
            oBingoCnt += 1
        if board[0][k] == board[1][k] == board[2][k] == 'X':
            xBingoCnt += 1


    # 대각선 방향 비교
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        oBingoCnt += 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        oBingoCnt += 1
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        xBingoCnt += 1
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        xBingoCnt += 1

    if oBingoCnt == 0 and xBingoCnt != 0 and xCnt < oCnt:
        return 0
    if oBingoCnt != 0 and xBingoCnt == 0 and xCnt >= oCnt:
        return 0
    elif oBingoCnt != 0 and xBingoCnt != 0:
        return 0
    else:
        return 1

    return answer
