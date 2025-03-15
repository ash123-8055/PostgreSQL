CREATE TABLE table1 (
    id int PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

CREATE TABLE table2 (
    id INT PRIMARY KEY,
    city VARCHAR(50),
    country VARCHAR(50),
    FOREIGN KEY (id) REFERENCES table1(id)
);

INSERT INTO table1 (id, name, age) VALUES 
(1, 'Alice', 25),
(2, 'Bob', 30),
(3, 'Charlie', 35),
(4, 'David', 40),
(5, 'Eve', 28);

INSERT INTO table2 (id, city, country) VALUES 
(1, 'New York', 'USA'),
(2, 'London', 'UK'),
(3, 'Berlin', 'Germany'),
(4, 'Paris', 'France'),
(5, 'Tokyo', 'Japan');

