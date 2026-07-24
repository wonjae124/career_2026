/*
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131529

주어진 정보
- 테이블 한 개
- 컬럼 3개(2개는 INTEGER, 1개는 VARCHAR)
- 전부 Nullable임. 따라서 NULL처리 안해줘도 됨.

풀어야 하는 것
- 상품 카테고리 코드를 그룹으로 묶어서 출력
- 상품 카테고리 코드는 오름차순 정렬

몰랐던 것
- GROUP by에 줘야하는 값은, select에서의 alias값임
-
*/

SELECT
SUBSTR(PRODUCT_CODE, 1, 2) as CATEGORY,
COUNT(*) AS PRODUCTS
from PRODUCT
group by CATEGORY;