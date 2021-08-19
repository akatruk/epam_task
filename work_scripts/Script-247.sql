drop table epam;
create table epam
(
id serial,
country_code varchar null,
date_value date null,
confirmed varchar null,
deaths varchar null,
stringency_actual numeric(10, 5) null,
stringency numeric(10, 5) null
)

select * 
from epam
where country_code = 'ALB';

group by country_code 
having country_code >= 1;

truncate table epam;

with cte1 as (
select distinct country_code, date_value, confirmed, deaths, stringency_actual, stringency
from epam e)
select * from cte1
order by deaths::int desc;

SELECT 
FROM public.epam;
