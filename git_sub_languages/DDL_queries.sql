#Creating a Table "employee" with values of id, fname, lname, age
create table employee(id varchar(10),fname varchar(30),lname varchar(30),age int,Primary Key(id))

#Adding new column to the table
alter table employee add column salary int;

#removes all data and only the structure remains
truncate table employee;

#Creating a Table "employee" with values of id, fname, lname, age
create table employee(id varchar(10),fname varchar(30),lname varchar(30),age int,Primary Key(id))
