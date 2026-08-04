'''
풀이
짝수번째는 대문자로, 홀수번째는 소문자로 반환

0123456789 10 11 12 13 14
try hello  w  o  r  l  d
TrY HeLlO  W  o  R  l  D

Try HeLlo WoRlD

upper, lower


'''
def solution(s):
    answer = ''

    s = s.split(' ')

    for word in s:
        temp = ''
        for idx, character in enumerate(word): # 배열
            if idx % 2 == 0: # 짝수
                temp += character.upper()
       else:
	    		temp += character.lower()
    	answer = ' '.join([answer, temp])

    return answer[1:]

print(solution("try hello world"))




