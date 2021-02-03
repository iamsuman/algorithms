# Write your MySQL query statement below
update salary
SET sex = (CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END)
