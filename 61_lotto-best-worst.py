'''
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/77484

answer는 최고 순위, 최저 순위가 담긴 배열임 정렬한 값으로 비교를 시작하기.

민우 0, 0, 1, 25, 31, 44임. 당첨 1, 6, 10, 19, 31, 45임.


순서에 상관 없으면 딕셔너리 사용해도 뭐... 근데 그 전에 일단 for문 부터;

=========== 시나리오,

원래부터 2개 일치해서 최소 5등임. 지금 모르는 번호 2개인데, 최고 순위 : 2개 다 일치하면 총 4개 일치하므로, 3등 최저 순위 : 0개 일치, 총 2개 일치하므로, 5등.

최저 순위는 그냥 쉽네. 기본 순위를 넣어주면 됨. 최고 순위는 0의 개수만큼 카운팅 더해주면 안되나?

변수 종류
- rank : 등수 배열
- rank의 인덱스 : correct_count
- unknown_count = 0의 개수 카운팅 수
- correct_count = 기존에 일치하는 개수
- precise_lottos = 번호 확인 가능한 로또 배열

'''

def solution(lottos, win_nums): 
    answer = [] 
    print(f'민우가 가진 배열 값 :{lottos}') 
    print(f'당첨 번호 값 : {win_nums}')

    unknown_count = lottos.count(0)

    correct_count = 0
    precise_lottos = [val for val in lottos if val != 0] 
    print(f'민우가 확실하게 알아볼 수 있는 로또 번호:{precise_lottos}')

    rank = [6, 6, 5, 4, 3, 2 ,1]

    for num in precise_lottos: 
        if num in win_nums: correct_count += 1


    minimum_grade = rank[correct_count]
    maximum_grade = rank[correct_count+unknown_count]
    print(f'민우의 최소 등수 : {minimum_grade}')
    print(f'민우의 최고 등수 : {maximum_grade}')

    answer.append(maximum_grade)
    answer.append(minimum_grade)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3,5] 
print(solution([0,  0, 0, 0, 0, 0],  [38, 19, 20, 40, 15, 25]))  # [1,6] 
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))   # [1,1]