-- 1. create the table definitions
-- 2. use the SQL COPY command to load the CSV files into the database


CREATE TABLE categories(
    categoryID INT not null,
    categoryName TEXT,
    description TEXT,
    picture TEXT 
);

CREATE TABLE customers(
    customerID TEXT,
    companyName TEXT,
    contactName TEXT,
    contactTitle TEXT,
    address TEXT, 
    city VARCHAR(50),
    region VARCHAR(25),
    postalCODE TEXT,
    country TEXT,
    phone VARCHAR(25),
    fax VARCHAR(25)
);

CREATE TABLE employees(
    employeeID INT,
    lastName TEXT,
    firstName TEXT,
    title TEXT,
    titleOfCourtesy TEXT,
    birthday TIMESTAMP,
    hireDate TIMESTAMP,
    address TEXT,
    city VARCHAR(50),
    region VARCHAR(50),
    postalCODE VARCHAR(15),
    country VARCHAR(25),
    homePhone VARCHAR(25),
    extension INT,
    PHOTO TEXT 
);
CREATE TABLE employee_territories(
    employeeID INT not null, 
    territoryID INT
);

CREATE TABLE order_details(
    orderID INT not null,
    productID INT not null, 
    unitPrice NUMERIC not null, 
    quantity INT not null, 
    discount NUMERIC
);

CREATE TABLE orders(
    orderID INT not null,
    customerID TEXT, 
    employeeID INT not null, 
    orderDate TIMESTAMP, 
    requiredDate TIMESTAMP,
    shippedDate TEXT,
    shipVia INT not null,
    freight NUMERIC not null,
    shipName TEXT, 
    shipAddress TEXT, 
    shipCity VARCHAR(30),
    shipRegion VARCHAR(20),
    shipPostalCode VARCHAR(15),
    shipCountry VARCHAR(50)
);

CREATE TABLE products(
    productID INT not null, 
    productName TEXT, 
    supplierID INT not null, 
    categoryID INT not null, 
    quantityPerUnit TEXT,
    unitPrice NUMERIC not null,
    unitsInStock INT not null,  
    unitsOnOrder INT not null, 
    reorderLevel INT not null,
    discontinued INT not null 
);

CREATE TABLE regions(
    regionID INT not null,
    regionDescription VARCHAR(20)
);

CREATE TABLE shippers(
    shipperID INT not null,
    companyName TEXT,
    phone VARCHAR(30)
);

CREATE TABLE suppliers(
    supplierID INT not null,
    companyName TEXT, 
    contactName TEXT, 
    contactTitle TEXT, 
    address TEXT, 
    city TEXT,
    region TEXT,
    postalCode TEXT,
    country TEXT,
    phone VARCHAR(50),
    fax VARCHAR(50),
    homePage TEXT
);

CREATE TABLE territories(
    territoryID INT not null,
    territoryDescription TEXT,
    regionID INT not null
);

\copy categories FROM 'data/categories.csv' DELIMITER ',' CSV HEADER;
\copy customers FROM 'data/customers.csv' DELIMITER ',' CSV HEADER;
\copy employees FROM 'data/employees.csv' DELIMITER ',' CSV HEADER;
\copy employee_territories FROM 'data/employee_territories.csv' DELIMITER ',' CSV HEADER;
\copy order_details FROM 'data/order_details.csv' DELIMITER ',' CSV HEADER;
\copy orders FROM 'data/orders.csv' DELIMITER ',' CSV HEADER;
\copy products FROM 'data/products.csv' DELIMITER ',' CSV HEADER;
\copy regions FROM 'data/regions.csv' DELIMITER ',' CSV HEADER;
\copy shippers FROM 'data/shippers.csv' DELIMITER ',' CSV HEADER;
\copy suppliers FROM 'data/suppliers.csv' DELIMITER ',' CSV HEADER;
\copy territories FROM 'data/territories.csv' DELIMITER ',' CSV HEADER;