/*
이름 : 입양 시각 구하기(1)
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59412

시간대 별로 모아서 조회를 해야한다.
근데 그걸 어떻게 절단을 시키지?...
시간대순으로 정렬시키게 해야한다.
뭐 DATETIME에서 시간대 부분만 끊어서 새로운 기준을 만든
다음에 그룹핑 해야지.

몰랐던 것
: 내가 임의로 만들어낸 별칭을 계속 활용할 순 없다.
: 단일행 연산은 숫자형, 문자형, 날짜형 등의 내장 함수임. SELECT, ORDER BY, GROUP BY, WHERE 어디에서든 사용 가능함. 단 하나의 행을 입력받아 단 하나만 출력하는 특징이 있음. 다중행 연산은 집계로 여러 값들을 동시에 입력받아서 하나의 결과를 출력한다.
: SQL의 논리적 실행 순서
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY (윈도우 함수, 집계 함수 사용 가능)

풀이 시간 : 2026.07.23. 23:30~
*/

SELECT
HOUR(DATETIME) AS HOUR,
COUNT(*)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)
