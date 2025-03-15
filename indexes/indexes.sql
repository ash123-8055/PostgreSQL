create index idx_name on table1 (name);

create index idx_name_age on table1(name,age); 

select * from pg_indexes where tablename='table1';

