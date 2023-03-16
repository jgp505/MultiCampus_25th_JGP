# SQL 용어 정리

# 목차
1. 데이터 베이스 구축법
2. 테이블 만들기
3. 조건문 & 순서 정리
4. 파이썬 연동

# 01. 데이터 베이스 구축법
   1. Schemas 진입 후, Create Schema 누르기
   2. 이름 지정
   3. 탭 닫기(ctrl + w)

# 02. 테이블 만들기
    1. SCHEMAS에 형성된 DB를 열어 Tables를 누른다.
    2. 오른쪽 마우스를 눌러 'Create Table' 누르기 
    3. Colum Name (열 이름)과 Datatype(데이터 형식)을 채워준다.
    
## 데이터 타입의 종류
- CHR(number) : number 갯수 만큼 입력 가능한 string 데이터 타입
- INT(number) : number 갯수 만큼 입력 가능한 int 데이터 타입
- DATE : datetime 데이터 타입

## 체크 박스
- PK(PRIMARY KEY) : 인덱스 지정 박스
- NN(Not Null) : 빈 데이터를 허용 안함

## 스크립트 형태
marker_db를 만든다고 가정을 해보자 
```sql
DROP DATABASE IF EXISTS market_db; -- 만약 market_db가 존재하면 우선 삭제한다.
CREATE DATABASE market_db; -- Database 구축
USE market_db;

-- Table 구축
-- 작성법 : ID  이름 [데이터 타입] [체크 박스]
CREATE TABLE member -- 회원 테이블
( mem_id  		CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  mem_name    	VARCHAR(10) NOT NULL, -- 이름
  mem_number    INT NOT NULL,  -- 인원수
  addr	  		CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  phone1		CHAR(3), -- 연락처의 국번(02, 031, 055 등)
  phone2		CHAR(8), -- 연락처의 나머지 전화번호(하이픈제외)
  height    	SMALLINT,  -- 평균 키
  debut_date	DATE  -- 데뷔 일자
);

CREATE TABLE buy -- 구매 테이블
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   mem_id  	CHAR(8) NOT NULL, -- 아이디(FK)
   prod_name 	CHAR(6) NOT NULL, --  제품이름
   group_name 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 가격
   amount    	SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (mem_id) REFERENCES member(mem_id)
);
```
# 03. 조건문 & 순서 정리
## SELECT 와 FROM
SELECT와 FROM은 Database에 있는 특정 테이블를 볼 수 있게 해주는 역할을 한다.
```sql
SELECT [열 이름] FROM [테이블 이름]

-- 예시
SELECT addr, mem_member FROM member_db -- member_db 테이블에서 addr, mem_member 열을 호출한다.

SELECT * FROM market_db.product -- maker_db 안에  product 테이블에 모든 열을 호출한다.
SELECT product_name FROM CLASSMODEL.PRODUCT -- CLASSMODEL 안에 RPODUCT 테이블에서 prdocut_name 열을 호출한다.
```

## WHERE, IN, LIKE
- WHERE : IF문 
- IN : IF문에서 조건이 많다면 IN을 사용해 줄일 수 있다.
- LIKE : `%` 나 `_` 를 사용하여 단어 개수나 포함된 단어를 찾아준다.

```sql
SELECT [열 이름] FROM [Table name] WHERE [조건문]
-- WHERE 예시
SELECT * FROM member WHERE mem_name='아이유'; -- mem_name에 아이유 이름을 가진 member 테이블 모든 열을 호출
SELECT mem_name, height, mem_number FROM member WHERE height >= 165 AND mem_number > 6 -- 키가 165 이상이며 mem_number 가 6보다 큰 값을 가진 member 테이블에서 mem_name, height, mem_number 열을 호출
SELECT * FROM member WHERE height BETWEEN 163 AND 165; -- 키가 163에서 165를 가진 member 테이블의 모든 열을 호출

SELECT [열 이름] FROM [Table name] WHERE [열 이름] IN(조건)
SELECT [열 이름] FROM [Table name] WHERE [열 이름] LIKE '조건'
-- IN과 LIKE 예시
SELECT * FROM member WHERE addr='경기' or addr='전남' or addr='경남' -- IN을 사용하지 않은 조건
SELECT * FROM member WHERE addr IN('경기','전남','경남') -- IN을 사용한 조건
SELECT * FROM product WHERE produc_name LIKE '서울%' -- product 테이블에서 produc_name 열 중 서울이라는 말이 들어가면서 뒤에 글씨 상관 없이 포함된 단어 호출
SELECT * FROM product WHERE produc_name LIKE '%서울' -- product 테이블에서 produc_name 열 중 서울이라는 말이 들어가면서 앞에 글씨 상관 없이 포함된 단어 호출
SELECT * FROM member WHERE mem_name LIKE '__소녀' -- OO소녀에 대해 찾아라 단, 소녀는 포함되면서 뒤에 무조건 2글자가 들어가야한다.
```
