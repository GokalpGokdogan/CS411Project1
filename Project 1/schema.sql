CREATE TABLE customer (
    cid CHAR(5) PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    bdate DATE NOT NULL,
    city VARCHAR(20) NOT NULL,
    nationality VARCHAR(20) NOT NULL
);




-- customer
INSERT into customer VALUES ('C101', 'Gokalp Gokdogan', '1990-01-01', 'Ankara', 'Turkey');
INSERT into customer VALUES ('C102', 'Ali Eren', '1990-01-01', 'Istanbul', 'Turkey');


