insert into monthly_avg_count (location, sale_month, avg_sales, count_sales) 
SELECT 
	a.location,
	a.sale_month,
	a.avg_sales,
	a.count_sales
FROM
(
	with sales_month_trunc as (
		-- first subsetting the relevant data 
		select
			s.*,
			date_trunc('month', TO_TIMESTAMP('{{data_interval_start}}', 'YYYY-MM-DDTH24:MI:SS+00:00')) as sale_month
		from sales s
	)
	-- then grouping and summing sales
	select
		location,
		sale_month,
		avg(value) as avg_sales,
        count(value) as count_sales
	from sales_month_trunc smt
	join stores st 
	on smt.store_idx = st.idx
	group by
		location,
		sale_month
) as a
;