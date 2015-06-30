# Write your MySQL query statement below


select t1.Name
from Customers t1
left join Orders t2
on t1.Id = t2.CustomerId
where t2.CustomerId is null
;
