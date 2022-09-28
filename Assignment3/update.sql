INSERT INTO `user` (`id`, `username`, `password`,  `rollno`  ,   `email`) VALUES (1, 'Durai', 'durai2345', 'cse004','duraisiva@gmail.com');
INSERT INTO `user` (`id`, `username`, `password`, `rollno`, `email`) VALUES (2, 'siva', 'sivsiv12','cse006', 'siva@gmail.com');
select * from user;


--update the user table
update user  set rollno='19cse004' where id=1;


--deleting the user table
delete from user where  email='duraisiva@gmail.com';

--viewing the table

select * from user;
