-- 코드를 작성해주세요
select distinct(ID) as id, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS d
join SKILLCODES s
on s.NAME = 'python' or s.NAME = 'C#'
where (d.SKILL_CODE & s.CODE) > 0
order by ID