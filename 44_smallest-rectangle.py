'''
문제
: 최소직사각형

풀이
: max와 min 잘 활용하기



1 : 60 x 50, 50 x 60
2 : 30 x 70, 70 x 30
3 : 60 X 30, 30 X 60

4 : 80 X 40, 40 X 80


가로 : 3, 4, 5, 6, 7,  8 max는 8
세로 : 3, 4, 5, 6, 7, (8) 

너비, 높이를 어떻게든 회전 시켜서 큰걸로 변환한다.

입출력 예제
: 명함들을 적절히 회전시켜 겹쳤을 때, 3번째 명함(가로: 8, 세로: 15)이 다른 모든 명함보다 크기가 큽니다.

'''
def solution(sizes):
    answer = 0

    max_w = 0
    max_h = 0
    for w, h in sizes:

    	w, h = max(w, h), min(w, h)
    	# print(f'w: {w}, h: {h}')
    	max_w = max(max_w, w)
    	max_h = max(max_h, h)

    answer = max_w * max_h
    # print(f'anwer : {answer}')

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
