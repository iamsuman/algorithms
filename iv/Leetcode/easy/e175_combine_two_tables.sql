-- Person
create table Person (PersonId int, FirstName varchar(10), LastName varchar(10));

-- Address
create table Address (AddressId int, PersonId int, City varchar(10), State varchar(10));

-- Combine tables
-- Oracle
select p.FirstName, p.LastName, a.City, a.State
from Person p, Address a
where p.PersonId = a.PersonId (+);

-- mysql
/* Write your PL/SQL query statement below */
select p.FirstName, p.LastName, a.City, a.State
from Person p left join Address a
where p.PersonId =  a.PersonId;
