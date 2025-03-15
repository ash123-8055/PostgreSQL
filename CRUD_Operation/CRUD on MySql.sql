#CRUD Operations on SQL Workbench


#Creating a Table "employee" with values of id, fname, lname, age
create table employee(id varchar(10),fname varchar(30),lname varchar(30),age int,Primary Key(id))

#Inserting 3 values into the table
insert into employee(id,fname,lname,age) values(1,"Ash","K",20),(2,"Ashwin","Kumar",21),(3,"A","K",22);  

#Reading the values from the table
select * from employee;

#Modifying the values in the table
update employee set age=30 where id="1";

#Deleting a value from the table
delete from employee where id="3";