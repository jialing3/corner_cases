# Write your MySQL query statement below

select distinct t1.Num
from Logs t1
join Logs t2
on t1.Num = t2.Num
join Logs t3
on t1.Num = t3.Num
where t1.Id + 1 = t2.Id and t2.Id + 1 = t3.Id
;
