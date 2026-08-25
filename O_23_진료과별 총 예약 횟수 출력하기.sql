-- 코드를 입력하세요
SELECT
MCDP_CD AS '진료과코드'
, COUNT(1) AS '5월예약건수'
FROM APPOINTMENT
WHERE SUBSTR(APNT_YMD,1, 7) = '2022-05'
GROUP BY MCDP_CD
ORDER BY COUNT(1), MCDP_CD
# 2022년 5월
# 진료과 코드별로 GROUP
# 환자 수 기준으로 오름차순, 진료과 코드 기준 오름차순