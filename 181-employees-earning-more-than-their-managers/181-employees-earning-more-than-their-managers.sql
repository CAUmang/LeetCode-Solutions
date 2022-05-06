# Write your MySQL query statement below
With CTE_new AS
(select e.name as ename, e.salary as esal, m.name as mname, m.salary as msal
from employee e
inner join employee m
on e.managerid = m.id)
select ename as Employee
from CTE_new
where esal>msal
;