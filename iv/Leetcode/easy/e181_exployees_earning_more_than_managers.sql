-- Employee TABLE
-- | Id | Name  | Salary | ManagerId |
select e.Name as Employee
# , e.Salary, m.Name, m.Salary
from employee e, employee m
where e.ManagerId = m.Id
and e.Salary > m.Salary;
