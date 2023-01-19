create table if not exists monthly_avg_count (
	location TEXT,
	sale_month DATE,
	avg_sales numeric(20,3),
    count_sales numeric(20,3)
)