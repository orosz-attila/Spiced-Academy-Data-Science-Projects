-- Analyzing The Northwind Dataset



-- 1. Get the names and the quantities in stock for each product. 
select productname, unitsinstock 
from products 
order by unitsinstock desc;


-- 2. Get a list of current products (Product ID and name).
select productid, productname 
from products 
where discontinued = 0;


-- 3. Get a list of the most and least expensive products (name and unit price). 
select productname, unitprice 
from products 
order by unitprice desc 
limit 20; 

select productname, unitprice 
from products 
order by unitprice asc 
limit 20;
    

-- 4. Get products that cost less than $20. 
select productname, unitprice 
from products 
where unitprice < 20 
order by unitprice desc;


-- 5. Get products that cost between $15 and $25. 
select productname, unitprice 
from products 
where unitprice 
between 15 and 25 
order by unitprice desc;


-- 6. Get products above average price. 
select productname, unitprice 
from products 
where unitprice > (SELECT AVG(unitprice) from products);


-- 7. Find the ten most expensive products. 
select productname, unitprice 
from products 
order by unitprice desc 
limit 10; 


-- 8. Get a list of discontinued products (Product ID and name). 
select productid, productname 
from products 
where discontinued = 1;


-- 9. Count current and discontinued products. 
select count(productname) 
from products 
where discontinued = 1;

select count(productname) 
from products 
where discontinued = 0;


-- 10. Find products with less units in stock than the quantity on order. 
select productname, unitsinstock, unitsonorder, (unitsinstock-unitsonorder) as difference 
from products 
order by difference asc;


-- 11. Find the customer who had the highest order amount 
SELECT companyname, city, ROUND(sum(od.unitprice * od.quantity)) AS total_revenue
FROM customers_csv AS c
JOIN orders_csv AS o ON o.customerid = c.customerid
JOIN order_details_csv AS od ON od.orderid = o.orderid
GROUP BY companyname, city
ORDER BY total_revenue desc;


-- 12. Find the hiring age of each employee
SELECT firstname, lastname, hiredate, birthdate, 
DATEDIFF(year, hiredate, birthdate) AS hiring_age 
FROM employees; 


-- 13. Selecting category and products name, join on categoryID  
SELECT categories.categoryname, products.productname
FROM categories
INNER JOIN products 
ON categories.categoryid = products.categoryid;


----------------------------------------------------------------


-- 1. which of our customers never made any orders?
SELECT companyname 
FROM 
orders ord RIGHT JOIN customers cus
ON ord.customerid = cus.customerid
WHERE orderid IS NULL;


-- 2. What is the average weight of all the orders, delivered to each country?
	-- e.g. 500 kg to Germany, 250 kg to Spain
	-- DO NOT USE THE ORDER COUNTRY , USE THE CUSTOMER COUNTRY 
	-- show the use of having 

SELECT cus.country, AVG(ord.freight) AS weight
FROM orders ord 
INNER JOIN
customers cus
ON ord.customerid = cus.customerid
GROUP BY cus.country
-- HAVING AVG(ord.freight) > 10 
-- AND cus.country IN ('Germany', 'Spain')
ORDER BY weight DESC;


-- 3. What is the total revenue delivered to each country?
   -- e.g. total money made from all orders to each country
	-- DO NOT USE THE ORDER COUNTRY, USE THE CUSTOMER COUNTRY

SELECT 
	SUM(det.unitprice * det.quantity * (1 - det.discount)) AS revenue, 
	cus.country
FROM order_details det
    -- a double join!!
	INNER JOIN orders ord
	ON det.orderid = ord.orderid
	INNER JOIN customers cus
	ON ord.customerid = cus.customerid
GROUP BY cus.country
ORDER BY revenue DESC;


-- 4. Suppliers/Vendors: who supplies to the company.
SELECT supplierid, companyname
FROM suppliers
ORDER BY supplierid asc;


-- 5. Sales Order transactions: details of the transactions taking place between the customers & the company.
SELECT od.orderid, c.companyname, p.productname, od.unitprice, od.quantity, od.discount
FROM order_details as od
LEFT JOIN products as p ON p.productid =od.productid
LEFT JOIN orders as o ON o.orderid = od.orderid
LEFT JOIN customers as c ON c.customerid = o.customerid;


-- 6. Which employee is making the most money?
SELECT 
	e.lastname || ', ' || e.firstname AS name, 
	e.title, 
	e.hiredate, 
	ROUND(sum(od.unitprice * od.quantity)) AS total_revenue
FROM employees AS e
JOIN orders AS o ON o.employeeid = e.employeeid
JOIN order_details AS od ON od.orderid = o.orderid
GROUP BY lastname, firstname, e.title, e.hiredate
ORDER BY total_revenue desc;


-- 7. Which company is the best customer?
SELECT 
	companyname, 
	city, 
	ROUND(sum(od.unitprice * od.quantity)) AS total_revenue
FROM customers AS c
JOIN orders AS o ON o.customerid = c.customerid
JOIN order_details AS od ON od.orderid = o.orderid
GROUP BY companyname, city
ORDER BY total_revenue desc;


-- 8. Where do the best customers come from?
SELECT 
	city, 
	ROUND(sum(od.unitprice * od.quantity)) AS total_revenue
FROM customers AS c
JOIN orders AS o ON o.customerid = c.customerid
JOIN order_details AS od ON od.orderid = o.orderid
GROUP BY city
ORDER BY total_revenue desc;


-- 9. Which products generate the most/least revenue?

SELECT  
	p.productname, 
	cat.categoryname, 
	ROUND(sum(od.unitprice * od.quantity)) AS total_revenue, 
	COUNT(o.orderid) AS nr_purchases, 
	p.unitsinstock, 
	p.unitsonorder, 
	p.discontinued
FROM orders AS o
JOIN order_details AS od ON od.orderid = o.orderid
JOIN products AS p ON p.productid = od.productid
JOIN categories AS cat ON cat.categoryid = p.categoryid
GROUP BY productname, categoryname, unitsinstock, unitsonorder, discontinued
--HAVING unitsinstock < 3
ORDER BY total_revenue asc;


-- 10. Which categories gerate the most/least revenue?

SELECT 
cat.categoryname, 
ROUND(sum(od.unitprice * od.quantity)) AS total_revenue, 
COUNT(o.orderid) AS nr_purchases  
FROM orders AS o
JOIN order_details AS od ON od.orderid = o.orderid
JOIN products AS p ON p.productid = od.productid
JOIN categories AS cat ON cat.categoryid = p.categoryid
GROUP BY categoryname
ORDER BY total_revenue asc;