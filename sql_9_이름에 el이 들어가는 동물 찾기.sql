# 이름에 el 포함. 단 대소문자 구분X, 이름 순으로 조회하되 이름이 같으면 아이디 기준 조회

-- 코드를 입력하세요
SELECT
    ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE LOWER(NAME) LIKE '%el%'
  AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME, ANIMAL_ID;