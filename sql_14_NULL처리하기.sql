-- 코드를 입력하세요
# 아이디 순으로 조회하는 SQL문 작성
# 이름이 없는 동물의 이름은 No Name으로 대체해서 넣기.

SELECT
ANIMAL_TYPE
, IFNULL(NAME, 'No name')
# , CASE
#     WHEN NAME IS NOT NULL THEN NAME
#     WHEN NAME IS NULL THEN 'No name'
#   END AS NAME
, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

