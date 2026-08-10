-- 물고기의 종류가 실제 잡은 숫자라는걸 헷갈림. 즉, 물고기의 구분을 잡은 숫자로 구분하고 있음.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/298518

SELECT
    count(1) AS FISH_COUNT
FROM FISH_INFO A
         LEFT JOIN FISH_NAME_INFO B
                   ON A.FISH_TYPE = B.FISH_TYPE
WHERE B.FISH_NAME IN ('BASS', 'SNAPPER')
