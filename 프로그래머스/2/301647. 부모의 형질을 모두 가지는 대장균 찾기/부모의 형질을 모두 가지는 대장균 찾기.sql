-- 코드를 작성해주세요
select e.ID, e.GENOTYPE, e1.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA e
join ECOLI_DATA e1
on e.PARENT_ID = e1.ID
where e.GENOTYPE & e1.GENOTYPE = e1.GENOTYPE
order by e.ID