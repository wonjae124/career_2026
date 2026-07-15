/*
배경
- 테이블 1개
- 5개의 컬럼
- 환자 정보 조회
주어진 정보
- 환자번호, 환자이름, 성별코드, 나이, 전화번호
Nullable인건 전화번호만임. 나머지는 None Nullable임.

접근 법
- 12세 이하인
- 여자인
- 전화번호가 없으면 NONE으로 대체
- 정렬 순서는 나이 내림차순, 환자이름 오름차순

몰랐던 것
- order by 여러 개 나오면 콤마로 구분
- 동등비교는 ==가 아니라 =라는 것
- NULL처리는 IFNULL로 하면 된다는 것

*/

select

PT_NAME,
PT_NO,
GEND_CD,
AGE,
IFNULL(TLNO, 'NONE') as TLNO
from PATIENT
where GEND_CD = 'W'
and AGE <= 12
order by age desc, pt_name asc;