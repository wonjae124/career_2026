'''
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12977

nums의 숫자를 합쳐서 만들 수 있는 소수의 개수.
소수는 자기 자신과 1 이외에는 공약수가 없어야 함.
따라서 공약수를 구하고, 공약수의 개수가 2개이면 소수이다. 2개가 아니면 소수가 아니다.
(Q: 1은 소수였나?, A: 2보다 작으면 prime이 아님.)
루트 씌우고, int로 바꾸고, 그 안의 값들을 for문으로 돌면서..
그 안의 값이 있으면 소수라서 참, 없으면 소수가 아니라서 거짓.

언제까지 하나면, nums의 값을 모두 사용하기 전까지 함.
nums 중에 3개의 수를 사용 함.


len, range, is_prime 함수 잘 쓰는게 중요함.

'''

def is_prime(num):
    print(f'소수 확인을 위해서 입력받은 수 : {num}')
    # ex) num = 4,
    # ex) num = 7
    if num < 2: 
        # 2부터 소수임.
        return False

    for value in range(2, int(num**0.5) + 1):
        # print(f'공약수 확인을 위한 수 : {value}')
        # num=8이면 1,2,4,8로 공약수의 개수가 2가 아닌 4개라서 소수가 아님.
        # num=7이면, 1,7로 공약수의 개수가 2개라서 소수임. 근데 왜 2부터 확인하지?
        if (num % value) == 0:
            # print(f'소수가  {value} 입니다')
            print(f'공약수 확인을 위한 수 : {num}, 현재 나누는 수 : {value}')
            return False

    return True

def solution(nums):
    # answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    count = 0
    n = len(nums)

    # 슬라이딩 루프
    for i in range(n-2): # 배열이므로 하나 
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                print(f'{nums[i]}, {nums[j]}, {nums[k]}')
                if is_prime(nums[i] + nums[j] + nums[k]):
                    count +=1

    return count

print(solution([1,2,3,4]))   # 1
print(solution([1,2,7,6,4])) # 4