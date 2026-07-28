/*

이름 : 헤비 유저가 소유한 장소
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/77487


공간을 2개 이상 소유한 유저(HOST_ID)를 헤비 유저라고 함.
ID 순으로 오름차순으로 뽑는다.

몰랐던 것
- 서브 쿼리(내부 쿼리)
- DB는 원래 괄호 안의 내부 쿼리를 먼저 본다.
- 최종 결과는 원본 데이터의 컬럼을 뽑아야 한다. 집계 또는 요약을 하지 않는다. 따라서 서브 쿼리를 쓰는 이유는 조건에 부합하는 HOST_ID만 뽑아낸다.
- 동명 동물은 서브 쿼리를 안 쓰는 이유 : 걔네는 집계를 하기 때문임.

풀이 시작 일자 : 26.07.23(목), 22:00
*/


SELECT
*
FROM PLACES
WHERE HOST_ID IN
(
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
)
ORDER BY ID