'''
문제 : 예산
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12982

고민
- 배열d를 전부 돌면서 값을 뽑는다.
언제까지? budget의 합계의 값을 넘기 전까지!
그 전까지는... 최대가 될 때까지 뽑아야 한다.
그걸 어케 뽑을지 잘 모르겠다;;

d가 배열이니 일단 돈다는건 확실한데...
최대 몇 개를 뽑을지를 어떻게 카운팅하지?;;
d[0]+d[1]+d[3] < budget      O, current=3
d[0]+d[1]+d[3]+d[4] < budget X, current=3에서 정지
answer = max(answer, current)

3개를 뽑는 경우와 4개를 뽑는 경우로 케이스를 나눠야 하나?...
절대 넘치면 안된다는건데;;
최대 d의 길이만큼 뽑으면 되겠다.

예외 사항
- 없는데?.... 안 보이는디?...

몰랐던 점
- combination은 문제 조건의 범위가 아주 작을 때 가능하다. d의 범위가 1~10 정도일 때 가능
- 그리디 사고 방식 필요함.
목표 : 한정된 예산으로 '최대한 많은' 부서를 지원
접근 : 당장의 최선의 선택. 가장 많은 부서를 채우려면, 무조건 가장 싼 부서부터 지원
행동 : 배열을 오름차순으로 정렬한 뒤, 제일 저렴한 부서부터 예산이 바닥날 때까지 차례대로 고르자.

문제 유형 : 완전 탐색이 아닌 그리디임.

풀이 시점 : 26.07.24, 09:50 ~
'''

def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in d:
        total += i
        if total <= budget:
            answer += 1
        else:
            break

    return answer