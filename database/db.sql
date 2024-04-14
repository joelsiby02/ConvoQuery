-- Create the database
CREATE DATABASE IF NOT EXISTS team6;
USE team6;

-- Create the t_shirts table
CREATE TABLE IF NOT EXISTS t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
    size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL,
    price DECIMAL(10, 2) CHECK (price BETWEEN 10 AND 50),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create the discounts table
CREATE TABLE IF NOT EXISTS discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    t_shirt_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100)
);

-- Create the orders table
CREATE TABLE IF NOT EXISTS orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    CustomerName VARCHAR(100),
    Email VARCHAR(100),
    Address VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(2),
    ZipCode VARCHAR(10),
    TShirtID INT,
    Design VARCHAR(50),
    Size VARCHAR(5),
    Color VARCHAR(20),
    Price DECIMAL(10, 2)
);

-- Create a stored procedure to populate the t_shirts table
DELIMITER $$
CREATE PROCEDURE PopulateTShirts()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 100;
    DECLARE brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas');
    DECLARE color ENUM('Red', 'Blue', 'Black', 'White');
    DECLARE size ENUM('XS', 'S', 'M', 'L', 'XL');
    DECLARE price DECIMAL(10, 2);
    DECLARE stock INT;

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values
        SET brand = ELT(FLOOR(1 + RAND() * 4), 'Van Huesen', 'Levi', 'Nike', 'Adidas');
        SET color = ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White');
        SET size = ELT(FLOOR(1 + RAND() * 5), 'XS', 'S', 'M', 'L', 'XL');
        SET price = ROUND(10 + RAND() * 40, 2);
        SET stock = FLOOR(10 + RAND() * 91);

        -- Attempt to insert a new record
        -- Duplicate brand, color, size combinations will be ignored due to the unique constraint
        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;  -- Handle duplicate key error
            INSERT INTO t_shirts (brand, color, size, price, stock_quantity)
            VALUES (brand, color, size, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to populate the t_shirts table
CALL PopulateTShirts();

-- Create a stored procedure to populate the discounts table
DELIMITER $$
CREATE PROCEDURE PopulateDiscounts()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 10;
    DECLARE t_shirt_count INT;
    DECLARE t_shirt_id INT;
    DECLARE pct_discount DECIMAL(5, 2); -- Moved the declaration outside the loop

    -- Get the total count of t-shirts
    SELECT COUNT(*) INTO t_shirt_count FROM t_shirts;

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values for t-shirt ID and discount percentage
        SET t_shirt_id = 1 + FLOOR(RAND() * t_shirt_count);
        SET pct_discount = ROUND(RAND() * 100, 2);

        -- Attempt to insert a new record
        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;  -- Handle duplicate key error
            INSERT INTO discounts (t_shirt_id, pct_discount)
            VALUES (t_shirt_id, pct_discount);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to populate the discounts table
CALL PopulateDiscounts();

-- Create a stored procedure to generate random orders
DELIMITER $$
CREATE PROCEDURE GenerateRandomOrders()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 1000;
    DECLARE customer_count INT;
    DECLARE tshirt_count INT;
    DECLARE customer_id INT;
    DECLARE tshirt_id INT;
    DECLARE order_date DATE;
    DECLARE price DECIMAL(10, 2);

    -- Get the total count of customers and t-shirts
    SET customer_count = 1000; -- Set the customer count to a desired value
    SELECT COUNT(*) INTO tshirt_count FROM t_shirts;

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values for customer ID and t-shirt ID
        SET customer_id = 1 + FLOOR(RAND() * customer_count);
        SET tshirt_id = 1 + FLOOR(RAND() * tshirt_count);

        -- Generate random order date within the last 3 years
        SET order_date = DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 365 * 3) DAY);

        -- Retrieve the price of the selected t-shirt
        SELECT price INTO price FROM t_shirts WHERE t_shirt_id = tshirt_id;

        -- Insert random order into orders table
        INSERT INTO orders (OrderDate, CustomerID, CustomerName, Email, Address, City, State, ZipCode, TShirtID, Design, Size, Color, Price)
        VALUES (order_date, customer_id, CONCAT('Customer', customer_id), CONCAT('customer', customer_id, '@example.com'), CONCAT('Address', customer_id), CONCAT('City', customer_id), CHAR(65 + (RAND() * 26)), LPAD(FLOOR(RAND() * 10000), 5, '0'), tshirt_id, CONCAT('Design', tshirt_id), ELT(FLOOR(1 + RAND() * 5), 'XS', 'S', 'M', 'L', 'XL'), ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White'), price);

        SET counter = counter + 1;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to generate random orders
CALL GenerateRandomOrders();
