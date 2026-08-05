-- 코드를 입력하세요
# ANIMAL_OUTS에만 존재하는 ANIMAL_ID를 골라야함.
# 가장 보호소에서 오랫동안 머무른걸 확인 해야하니 DATETIME이 제일 큰걸로 고른다.
# DATETIME이 내림차순이 되게한다.

SELECT
      NAME
    , DATETIME
  FROM ANIMAL_INS
 WHERE ANIMAL_ID NOT IN  (
    SELECT
        ANIMAL_ID
      FROM ANIMAL_OUTS
    )
ORDER BY DATETIME
limit 3;



