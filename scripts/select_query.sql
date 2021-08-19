with cte1 as (
select distinct country_code, date_value, confirmed, deaths, stringency_actual, stringency
from epam e)
select * from cte1
order by deaths::int desc;
