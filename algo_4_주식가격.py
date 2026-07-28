'''
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/42584
이름 : 주식가격
유형 : 완탐
난이도 : LEVEl2
푸는법
- O(N)이나 O(NlogN)으로 풀어야 함
아니, 가격이 떨어졌는지 안 떨어졌는지 어케 알지?;
각 인덱스의 시작을 기준으로 다음 인덱스에서 값이 떨어지지 않으면 유지기간이 1 증가하고, 떨어지면 그냥 바로 return 배열에 지금까지의 기간을 삽입하면 된다.
웬만하면 마지막 인덱스는 0이 될 수 밖에 없기 때문에, 마지막 인덱스 전 인덱스까지 돌면 된다.

몰랐던 것
스택처럼 풀어야 한다네?
가격이 오르거나 같은 경우에 스택에 그 인덱스를 넣는거고, 내린 경우에만 스택에서 제거하는건가보다.

시간 : 26.07.24. 10:50 ~ 14:05

'''

from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    stack = deque()

    '''
    case: [2, 2, 2, 2, 2]
    '''

    for current_index in range(len(prices)):
        if not stack: # 스택이 비어있으면 무조건 넣는걸로 시작하는 듯
            stack.append(current_index)
        else:
            # 스택 값이 있는걸 확인하는 이유? : stack[-1]의 스택 최상단 호출 에러 방지
            while prices[current_index] < prices[stack[-1]]:
                past_index = stack.pop()
                answer[past_index] = abs(current_index - past_index)
            stack.append(current_index)

    while stack:
        last_day = stack.pop()
        answer[last_day] = len(prices) - last_day - 1

    return answer