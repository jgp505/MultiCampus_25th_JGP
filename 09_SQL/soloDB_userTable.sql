DROP DATABASE IF EXISTS soloDB;
CREATE DATABASE soloDB;
USE soloDB;
CREATE TABLE userTable (id char(4),
 userName char(15), 
 email char(20), 
 birthYear int);
 
INSERT INTO userTable VALUES('hong' ,'홍지윤' , 'hong@naver.com', 1996);
INSERT INTO userTable VALUES('kim' , '김태연' , 'kim@daum.net', 2011);
INSERT INTO userTable VALUES( 'star' , '별사랑' , 'star@paran.com' , 1990);
INSERT INTO userTable VALUES( 'yang' , '양지은' , 'yang@gmail.com' , 1993);