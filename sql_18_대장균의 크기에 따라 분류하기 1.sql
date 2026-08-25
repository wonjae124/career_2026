-- 크기비교는 BETWEEN 말고도, 부등호(>=<)로 가능함. ELSE가 없으면 생략이 되며 NULL로 채워짐
-- https://school.programmers.co.kr/learn/courses/30/lessons/299307

SELECT
A.ID
, CASE
    WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
    WHEN SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
    WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH'
END AS SIZE
FROM ECOLI_DATA A
ORDER BY ID