'''
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/136798

number = 5, limit = 3, power = 2
자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매
약수 개수가 limit보다 큰 경우에는 power를 구매함.
1,   2,    3,   4,         5
1,  1,2,  1,3,  1,2,4,   1,5
 
약수의 개수를 세서, 그 값을 limit와 비교해서 더 크면,
power를 도입을 하는거다.


'''

def count_divisors(num):
    """Return the number of divisors of a given number."""
    
    count = 0
    
    # print(f"Number: {num}")
    # print(f"Square root of {num}: {num ** 0.5}")
    # print(f"We only need to check from 1 to {int(num ** 0.5)}")
    # print()

    for i in range(1, int(num ** 0.5) + 1):
        
        # print(f"Checking i = {i}")
        # print(f"{num} % {i} = {num % i}")

        if num % i == 0:
            # print(f"  -> {i} is a divisor!")
            
            count += 1
            # print(f"  -> count = {count}")

            paired_divisor = num // i
            # print(f"  -> Paired divisor: {num} // {i} = {paired_divisor}")

            if i != paired_divisor:
                count += 1
                # print(f"  -> {paired_divisor} is also a divisor!")
                # print(f"  -> count = {count}")
            # else:
                # print(f"  -> {i} and {paired_divisor} are the same, so don't count twice.")

        # else:
            # print(f"  -> {i} is NOT a divisor.")

        # print()

    # print(f"Total number of divisors of {num}: {count}")
    
    return count

# print(count_divisors(9))


def solution(number, limit, power):
    answer = 0
    answer_list = []

    print(f'기사의 최대 번호 number : {number}')
    print(f'기사의 최대 협얍 공격력 limit : {limit}')
    print(f'기사가 최대 공격력을 넘을 때 부여할 무기 공력 power : {power}')
    print(f'무기 만들기 위해 필요한 무게 최초 answer : {answer}')
    print()

    for i in range(1, number + 1):
        print(f'   현재 기사의 번호 i : {i}')
        origin_power = count_divisors(i)
        print(f'   현재 기사가 가질 수 있는 공격력 origin_power : {origin_power}')
        if origin_power > limit:
            print(f'        => 현재 기사의 공격력 {origin_power}가 협약으로 인한 공격력인 limit({limit}) 보다 클 경우 최대 공격력 power({power}) 부여')
            answer_list.append(power)
        else:
            print(f'        => 현재 기사의 공격력 {origin_power}가 협약으로 인한 공격력인 limit({limit}) 보다 낮으므로 타고난 공격력 origin_power({origin_power}) 부여')
            answer_list.append(origin_power)


    answer = sum(answer_list)

    print(f'무기 만들기 위해 필요한 최종 무게 answer : {answer}')

    return answer

print(solution(5, 3, 2))  # 10
print(solution(10, 3, 2)) # 21