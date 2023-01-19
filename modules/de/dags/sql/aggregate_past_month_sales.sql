insert into monthly_sales (store_idx, location, sale_month, value) 
SELECT 
	a.store_idx,
	a.location,
	a.sale_month,
	a.value
FROM
(
	with sales_month_trunc as (
		-- first subsetting the relevant data 
		select
			s.*,
			date_trunc('month', TO_TIMESTAMP('{{data_interval_start}}', 'YYYY-MM-DDTH24:MI:SS+00:00')) as sale_month
		from sales s
		where
			s.date >= to_timestamp('{{data_interval_start}}', 'YYYY-MM-DDTH24:MI:SS+00:00')
			and s.date < to_timestamp('{{data_interval_end}}', 'YYYY-MM-DDTH24:MI:SS+00:00')
	)
	-- then grouping and summing sales
	select
		st.idx as store_idx,
		location,
		sale_month,
		sum(value) as value
	from sales_month_trunc smt
	join stores st 
	on smt.store_idx = st.idx
	group by
		st.idx,
		location,
		sale_month
) as a
;
