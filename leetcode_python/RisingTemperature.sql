# Write your MySQL query statement below

select t1.Id
from Weather t1 -- today
join Weather t2 -- yesterday
on date_sub(t1.Date, interval 1 day) = t2.Date
where t1.Temperature > t2.Temperature
;
