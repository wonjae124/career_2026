/*
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/164668

주요 정보
    테이블 2개(A는 컬럼 8개, B는 컬럼 6개 중에 Nullable 하나)
    A는 중고 거래 게시판 정보
        - 가격, 거래상태, 작성자ID(WRITER_ID)
    B는 중고거래 게시판의 사용자 정보
        - 유저ID(USER_ID), 닉네임

풀어야 하는 정보
    완료된 거래
    거래 총 금액 70만원 이상
    총 거래 금액 오름차순


꺼내야 하는 정보
    아이디
    닉네임
    총 거래 금액

몰랐던 것
    집계함수(GROUP BY)사용 후 집계결과를 필터링하는게 있다는 것(HAVING)
    INNER JOIN의 ON은 WHERE의 뒤에 와야함.

*/

SELECT
    B.USER_ID
     , B.NICKNAME
     , SUM(A.PRICE) AS TOTAL_SALES
from USED_GOODS_BOARD A
         INNER JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
WHERE A.STATUS = 'DONE'
GROUP BY B.USER_ID, B.NICKNAME
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC;