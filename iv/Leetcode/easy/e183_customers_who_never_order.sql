-- Suppose that a website contains two tables,
-- the Customers table and the Orders table.
-- Write a SQL query to find all customers who never order anything.
-- Customers: | Id | Name  |
-- Orders: | Id | CustomerId |
select Name as Customers
from Customers
where Id not in (
select c.Id
from Customers c, Orders o
where c.Id = o.CustomerId);

