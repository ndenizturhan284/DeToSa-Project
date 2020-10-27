DROP DATABASE IF EXISTS boutique;
CREATE DATABASE boutique;
USE boutique;

-- {{{ Table Definitions
DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(16) NOT NULL,
    last_name VARCHAR(16) NOT NULL,
    phone_number VARCHAR(16) NOT NULL,
    size INTEGER NOT NULL,
    wedding_date DATETIME NOT NULL
);

DROP TABLE IF EXISTS dresses;
CREATE TABLE dresses(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    dress_name VARCHAR(16) UNIQUE NOT NULL,
    dress_size INTEGER NOT NULL
    -- available VARCHAR(16) NOT NULL
);

DROP TABLE IF EXISTS reservations;
CREATE TABLE reservations(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    dress_id INTEGER NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(dress_id) REFERENCES dresses(id),
    rent_date datetime,
    return_on DATETIME
);

-- Big brain idea: start the user ids at a nice big number so it looks like we have lots of users.
ALTER TABLE customers AUTO_INCREMENT=119;
ALTER TABLE dresses AUTO_INCREMENT=57;
ALTER TABLE reservations AUTO_INCREMENT=117;


-- {{{ Insert test data.
INSERT INTO customers VALUES (NULL, 'Emily', 'Smith', '123-456-7890','32','2021-01-01');
INSERT INTO customers VALUES (NULL, 'Sarah', 'Brown', '123-098-6543','40','2021-02-01');
INSERT INTO customers VALUES (NULL, 'Jenifer', 'Gold', '678-987-1234','36','2021-03-01');

INSERT INTO dresses VALUES (NULL, 'Deniz', '32');
INSERT INTO dresses VALUES (NULL, 'Tova', '40');
INSERT INTO dresses VALUES (NULL, 'Amanda', '34');
INSERT INTO dresses VALUES (NULL, 'Rachel', '36');
INSERT INTO dresses VALUES (NULL, 'Melanie', '38');

INSERT INTO reservations VALUES (NULL, '119', '57', '2021-01-01','2021-02-01');
INSERT INTO reservations VALUES (NULL, '120', '58', '2021-02-05',Null);
INSERT INTO reservations VALUES (NULL, '119', '57', '2021-02-03','2021-02-04');

