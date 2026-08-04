'''
풀이
5명 중 3명을 뽑음
3명의 합이 0이면 횟수 증가

무조건 3개 뽑아야 함.

순열/수열?
횟수 반환

for문 3개 돌아야 함.

'''
def solution(number):

    answer = 0
    for i in range(len(number)):
    	for j in range(i+1, len(number)):
    		for k in range(j+1, len(number)):
    			if number[i] + number[j] + number[k] == 0 :
    				# print(f'i: {i}/{number[i]}  j: {j}/{number[j]}, k : {k}/{number[k]}')
    				answer += 1
    return answer

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))




