'''
풀이
숫자 크기 비교 문제
주어진 P보다 작은 숫자일 경우 증가한다.

t에서 p의 개수만큼 뽑는다.
for문을 돌면서 뽑는다. temp 같은 변수하나 만들어서 p의 개수만큼 만든다.
만든 temp를 정수형으로 변환하고, 마찬가지로 변환한 정수형인 p와 비교한다.


'''
def solution(t, p):
    answer = 0

    for i in range(len(t)-len(p)+1):
    	temp = ''
    	for j in range(len(p)):
    		temp += t[i+j]
    	if int(temp) <= int(p):
    		# print(f'temp : {temp}')	
    		answer += 1

    return answer

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))