-- Simple View
create view salary_table as select * from employee where salary>=60000;

select * from salary_table;

-- Complex view
create view sample as select table1.id as table1_id, name,city,country from table1 join table2 on table1.id=table2.id where table1.id in (1,3,5);

select * from sample;