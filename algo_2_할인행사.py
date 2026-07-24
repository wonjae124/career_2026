'''
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131127?language=python3#

문제 배경
원하는 품목이 10일 안에 전부 나오는 날을 찾기. 품목 하나라도 부족하면 그 날은 안됨.

원하는 결과
부합하는 날의 개수를 반환하기.
만약 없으면 0 반환

제약 상황
원하는 품목 배열의 길이는 1 ~ 10개. 개수 배열과 서로 길이 같음.
할인 품목(discount)의 길이 10~100,000

예외 상황
여러 날짜인 경우엔 어카지?

접근법
내가 원하는 제품이 cnt를 만족하는 날(map으로 하면 되겠네)들을 구한다.

푸는법
문자열을 비교한다.
일단 뭐든 순서는 상관없다.
일단 want의 요소를 보고,

어차피 discount를 돌거긴하다. 근데 단방향이다.
돌 때의 범위 : 0 ~ len(discount) - (number 안의 총계)까지.
    ex) discount 14, number의 합 10, 14 - 10 = 4, 0 ~ 4까지 돌아야한다.

매핑을 어떻게 할 것인가? 딱 개수가 맞아야한다.
따라서, 매번 개수를 저장한 값을 초기화 해야한다.
근데 그게 실제로 있는 넘버링이 되어야 한다. 만약 넘버링은 0이 될 수 없다.

그래서 result 값은 어떻게 판단해서 계산하면 돼?

{
    "banana" : 3
    , "apple" : 2
    , "rice" : 2
    , "pork" : 2
    , "pot" : 1
}
temp 맵의 세팅은 discount 테이블을 돌 때마다 한다.
도는건, number 배열 내부의 총합횟수만큼 돌면 된다.
지금은 10이므로, 10번까지 전진하면 된다.
단, 마지막까지 10번까지 갔는데, 만약 tempMap의 모든 value들의 값이 0 이면,answer 값을 1 늘린다. 아니면 아무 것도 안하면 된다.
-> 해당 문법 모르겠어서, 그냥 마지막까지 다 확인한 경우에 answer을 1 증가

매핑할 때, real맵에 맞는 key가 없으면 for문을 다음으로 돌린다.
만약 key에 맞으면, temp의 맵을 보고 해당 key의 value를 -1 시킨다.
물론 그 key가 없을 수도 잇다는건 알아둬야 한다. key가 있는지는 확인한다.

(key가 이미 0이면 어떻하지?)


변수
- map으로 만들거
- tempMap 매번 새로운 map 만들어서 복사하기.(가능한가?... 깊은 복사는 안되어야 한다. 원본의 값은 바뀌면 안되는데 말이다. 이게 맞나? 내가 잘 알고 있는건가?)
- 최종 결과 개수, result

주의사항
- 괜히 index를 안 벗어나게 주의해야겠다.
- discount의 길이가 좀 많이 길다.
- 10^5개다. 이거는 O(N)이나, O(logN)만 허용한다.
- ㅓ

풀은 날짜
26.07.15, 18:24 ~ 26.07.16, 0:20

'''

import copy

def solution(want, number, discount):
    answer = 0
    real = {}
    want_cnt = len(want)
    discount_cnt = len(discount)
    number_cnt = len(number)
    number_sum = sum(number)
    check_day_boundary = discount_cnt - number_sum + 1

    for i in range(number_cnt):
        real[want[i]] = number[i]

    for k in range(0, check_day_boundary, 1):
        temp = copy.deepcopy(real)
        for p in range(number_sum):
            current_string = discount[k+p]
            # print(current_string)
            if current_string in temp.keys():
                if temp[current_string] <= 0:
                    # print(k, p, current_string) # 이거 안해주면, 이미 원하는만큼 구매한 물건도 그 날 추가 지출하는 사태 발생함. 즉, result가 1 늘어나는 상황 발생함. 결과는 점수 8점 나옴.
                    break
                temp[current_string] -= 1
                if p == (number_sum - 1):
                    answer += 1
            else:
                break
            # if all(val == 0 for val in temp.values()):
            # answer += 1

    return answer