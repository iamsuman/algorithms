# Write your MySQL query statement below
select p.project_id, e.employee_id
from Project p, Employee e,
(select p.project_id, max(e.experience_years) as experience_years
from Project p, Employee e
where p.employee_id = e.employee_id
group by p.project_id) as ey
where p.employee_id = e.employee_id
and p.project_id = ey.project_id
and e.experience_years = ey.experience_years;
