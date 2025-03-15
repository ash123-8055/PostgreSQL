#Inner Join
SELECT table1.id, table1.name, table1.age, table2.city, table2.country 
FROM table1 
INNER JOIN table2 ON table1.id = table2.id;

#Left Join
SELECT table1.id, table1.name, table1.age, table2.city, table2.country
FROM table1
LEFT JOIN table2 ON table1.id = table2.id;

#Right Join
SELECT table1.id, table1.name, table1.age, table2.city, table2.country
FROM table1
RIGHT JOIN table2 ON table1.id = table2.id;

#Full Outer join
SELECT table1.id, table1.name, table1.age, table2.city, table2.country
FROM table1
FULL OUTER JOIN table2 ON table1.id = table2.id;

#Cross Join
SELECT table1.id, table1.name, table1.age, table2.city, table2.country
FROM table1
CROSS JOIN table2;
