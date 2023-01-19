# Extra Tasks

## Instructions

You only need to implement one of these tasks!

## Tasks

* create an intermediary table, called `customer_activity_ranked`, that adds an additional `activity_rank` column to the customer activity table. This column has, **for each customer**, value 1 for the latest activity, 2 for the second latest, 3 for the third latest, and so forth.
* create a new database user, called `analyst`, with READ and WRITE access to the public schema of the database. This user should be created when starting the database for the first time.
* create a new DAG which you can trigger manually, and that prints to the console the following sales statistics: average sales value per month, and the number of sales per month, for each store.
