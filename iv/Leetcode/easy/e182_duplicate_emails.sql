-- Write a SQL query to find all duplicate emails in a table named Person.
-- Id | Email
select Email
--, count(*)
from Person
group by Email
having count(*) > 1;
