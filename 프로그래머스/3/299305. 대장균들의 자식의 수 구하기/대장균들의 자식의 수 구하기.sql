-- 코드를 작성해주세요
select e.ID, count(e1.ID) as CHILD_COUNT
from ECOLI_DATA e
left join ECOLI_DATA e1
on e.ID = e1.PARENT_ID
group by ID