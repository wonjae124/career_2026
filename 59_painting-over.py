def solution(n, m, section):

    count = 0
    visited = [False] * (n + 1)

    for sec in section:
        
        if visited[sec]:
            continue
        count += 1
        
        for j in range(sec, min(sec + m, n + 1)):
            visited[j] = True

    return count

print(solution(8, 4, [2, 3, 6]))  # Output: 2
print(solution(5, 4, [1, 3]))     # Output: 1
print(solution(4, 1, [1, 2, 3, 4])) # Output: 4

