create table if not exists feature_store as
select 
	cp.idx,
	cp.attr_a,
	cp.attr_b,
	cal.scd_a,
	cal.scd_b,
	l.label
from customer_profiles cp 
join customer_activity_latest cal 
	on cp.idx = cal.idx
join labels l 
	on cp.idx = l.idx 
;