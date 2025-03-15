#Creating a Table "employee" with values of id, fname, lname, age
create table employee(id varchar(10),fname varchar(30),lname varchar(30),age int,Primary Key(id))

#Inserting 3 values into the table
insert into employee(id,fname,lname,age) values(1,"Ash","K",20),(2,"Ashwin","Kumar",21),(3,"A","K",22);  

#Reading the values from the table
select * from employee;

#creating a save point
savepoint before_updation;

#Modifying the values in the table
update employee set age=30 where id="1";

#Rollback to previous state before updations
rollback to savepoint before_updation;

#creating a save point
savepoint before_deletion;

#Deleting a value from the table
delete from employee where id="3";

#Rollback to previous state before deletion
rollback to savepoint before_deletion;

#Saves all the changes
commit;