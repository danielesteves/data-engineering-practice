DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS account; 
DROP TABLE IF EXISTS product; 


CREATE TABLE IF NOT EXISTS account (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    address_1 VARCHAR(255) NOT NULL,
    address_2 VARCHAR(255),
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    zip_code INT NOT NULL,
    join_date DATE
);

CREATE TABLE IF NOT EXISTS product (
    product_id INT,
    product_code INT NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id, product_code)
);

CREATE TABLE IF NOT EXISTS transaction (
    transaction_id varchar(27) PRIMARY KEY,
    transaction_date DATE,
    product_id INT NOT NULL,
    product_code INT NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    account_id INT NOT NULL REFERENCES account (customer_id),
    FOREIGN KEY (product_id, product_code)
      REFERENCES product (product_id, product_code)
);