create table if not exists monthly_sales (
	store_idx INTEGER,
	location TEXT,
	sale_month DATE,
	value numeric(20,3)
)