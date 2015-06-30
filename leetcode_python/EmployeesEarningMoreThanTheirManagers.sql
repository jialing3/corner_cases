# Write your MySQL query statement below

select t1.Name
from Employee t1
join Employee t2
on t1.ManagerId = t2.Id
where t1.ManagerId is not NULL
and t1.Salary > t2.Salary
;
