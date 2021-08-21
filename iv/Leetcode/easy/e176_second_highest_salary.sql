-- Solution 1
select max(Salary) as SecondHighestSalary
from Employee
where Salary != (
select max(Salary)
from Employee
);

SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;

