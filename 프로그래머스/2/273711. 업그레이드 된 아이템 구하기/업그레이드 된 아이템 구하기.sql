-- 코드를 작성해주세요
select i.ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO i
join ITEM_TREE t
on i.ITEM_ID = t.ITEM_ID
where PARENT_ITEM_ID in (select ITEM_ID from ITEM_INFO where RARITY = 'rare')
order by i.ITEM_ID desc