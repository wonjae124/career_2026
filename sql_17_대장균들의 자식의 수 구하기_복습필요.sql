/*
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/299305
JOIN 결과
A.ID   B.ID
1      3

2      4
2      5

3      NULL

4      6

5      NULL
6      NULL

*/

SELECT
    A.ID
     , COUNT(B.ID) AS CHILD_COUNT
FROM ECOLI_DATA A
         LEFT JOIN ECOLI_DATA B # 자식이 없는 대장균도 B.ID를 NULL로 보여줘야 하기 때문임
ON A.ID = B.PARENT_ID # A 개체의 ID를 부모로 가지고 있는 B 개체를 찾아라.
    GROUP BY A.ID
ORDER BY ID