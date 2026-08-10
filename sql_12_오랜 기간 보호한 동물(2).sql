-- 코드를 입력하세요
WITH out1 AS (
    SELECT
        ANIMAL_ID
         , DATETIME
    FROM ANIMAL_OUTS
)
SELECT
    in1.ANIMAL_ID
     , in1.NAME
FROM ANIMAL_INS AS in1
         JOIN out1 ON out1.ANIMAL_ID = in1.ANIMAL_ID
ORDER BY (in1.DATETIME - out1.DATETIME)
    limit 2

/*
Best.
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME)
    LIMIT 2
    출처: https://shjz.tistory.com/114 [What matters the most to you, Why:티스토리]

*/