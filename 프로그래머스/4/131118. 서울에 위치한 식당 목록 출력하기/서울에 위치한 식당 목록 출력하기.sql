-- 코드를 입력하세요
SELECT REST_INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, round(avg(REVIEW_SCORE), 2) as score
from REST_INFO join REST_REVIEW
on REST_INFO.REST_ID = REST_REVIEW.REST_ID
where ADDRESS like '서울%'
group by REST_ID 
having count(*) > 0
order by SCORE desc, FAVORITES desc