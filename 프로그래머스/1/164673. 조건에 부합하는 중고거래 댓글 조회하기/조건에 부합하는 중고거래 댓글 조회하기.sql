SELECT TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, 
       date_format(r.CREATED_DATE,"%Y-%m-%d") as CREATED_DATE
from USED_GOODS_BOARD as b
join USED_GOODS_REPLY as r
on r.BOARD_ID=b.BOARD_ID
where year(b.CREATED_DATE) = 2022 
and month(b.CREATED_DATE) = 10
order by CREATED_DATE, TITLE asc

