DROP DATABASE IF EXISTS soloDB;
CREATE DATABASE soloDB;
CREATE TABLE `solodb`.`new_table` (
  `user_id` VARCHAR(5) NOT NULL,
  `user_name` VARCHAR(15) NOT NULL,
  `user_email` VARCHAR(20) NULL,
  `user_birthday` DATE NULL,
  PRIMARY KEY (`user_id`));
INSERT INTO `solodb`.`new_table` (`user_id`, `user_name`, `user_email`, `user_birthday`) VALUES ('1', '김태리', 'tlkim@gmail.com', '2018-03-01');
INSERT INTO `solodb`.`new_table` (`user_id`, `user_name`, `user_email`, `user_birthday`) VALUES ('2', '이병헌', 'bhkim@gmail.com', '2017-08-15');
INSERT INTO `solodb`.`new_table` (`user_id`, `user_name`, `user_email`, `user_birthday`) VALUES ('3', '송중기', 'jgsong@gmail.com', '2019-01-01');
INSERT INTO `solodb`.`new_table` (`user_id`, `user_name`, `user_email`, `user_birthday`) VALUES ('4', '송혜교', 'hksong@gmail.com', '2017-11-01');usertableusertable