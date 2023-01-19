create table customer_activity_latest as
with customer_activity_ranked as (
	select
		ca.*,
		rank() over (
			partition by idx
			order by valid_from desc
		) as r
	from customer_activity ca
)
select
	idx,
	valid_from,
	valid_to,
	scd_a,
	scd_b 
from customer_activity_ranked car
where car.r = 1;
