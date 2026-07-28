/*
문제 이름 : 동명 동물 수 찾기
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59041

동물 이름이 2번 이상 쓰인 경우의 이름과 그 횟수 조회
이름이 없는 동물은 제외
결과는 이름 순으로 오름차순으로 정렬

몰랐던 것 
: 무조건 서브 쿼리 쓰는 풀이가 아니다.
새롭게 MAX, AVG, SUM 등의 집계를 하거나, 더 추가적인 조건을 붙일 때 함.

풀이 일자 : 26.07.23 22:40 ~
*/

SELECT
NAME
, COUNT(*)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(*) >= 2
ORDER BY NAME