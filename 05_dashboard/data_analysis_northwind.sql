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