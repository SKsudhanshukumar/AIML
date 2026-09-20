-- Total Sales
SELECT
    SUM(sales) AS total_sales
FROM sales;

-- Total Orders
SELECT 
    COUNT(DISTINCT order_id) AS total_orders 
FROM sales;

-- Total customers
SELECT 
    COUNT(DISTINCT customer_id) AS total_customers 
FROM sales;

-- Total Products
SELECT 
    COUNT(DISTINCT product_id) AS total_products 
FROM sales;

-- Average Order value
SELECT 
    SUM(sales) / COUNT(DISTINCT order_id) AS average_order_value 
FROM sales;

-- Sales by year
SELECT 
    year, 
    SUM(sales) AS total_sales 
FROM sales 
GROUP BY year 
ORDER BY year;

-- Sales by month
SELECT 
    month, 
    month_name, 
    SUM(sales) AS total_sales 
FROM sales 
GROUP BY month, month_name 
ORDER BY month;

-- Sales by quarter
SELECT
    quarter,
    SUM(sales) AS total_sales
FROM sales
GROUP BY quarter
ORDER BY quarter;

-- Sales by region
SELECT
    region,
    SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- Sales by category
SELECT
    category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Sales by sub-category
SELECT
    sub_category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY sub_category
ORDER BY total_sales DESC;

-- Top 10 Product
SELECT
    product_name,
    SUM(sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- Customer segment analysis
SELECT
    segment,
    SUM(sales) AS total_sales,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS customers
FROM sales
GROUP BY segment
ORDER BY total_sales DESC;

-- Shipping mode analysis
SELECT
    ship_mode,
    COUNT(DISTINCT order_id) AS orders,
    SUM(sales) AS total_sales,
    ROUND(AVG(shipping_days), 2) AS avg_shipping_days
FROM sales
GROUP BY ship_mode
ORDER BY orders DESC;

-- Regional + category analysis
SELECT
    region,
    category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY region, category
ORDER BY region, total_sales DESC;

-- Monthly sales for each year
SELECT
    year,
    month,
    month_name,
    SUM(sales) AS total_sales
FROM sales
GROUP BY year, month, month_name
ORDER BY year, month;

-- Year-over-year growth
WITH yearly_sales AS (
    SELECT
        year,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY year
)

SELECT
    year,
    total_sales,
    LAG(total_sales) OVER (
        ORDER BY year
    ) AS previous_year_sales
FROM yearly_sales;

-- Calculate growth percentage
WITH yearly_sales AS (
    SELECT
        year,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY year
),

sales_with_previous AS (
    SELECT
        year,
        total_sales,
        LAG(total_sales) OVER (
            ORDER BY year
        ) AS previous_year_sales
    FROM yearly_sales
)

SELECT
    year,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(previous_year_sales, 2) AS previous_year_sales,
    ROUND(
        (total_sales - previous_year_sales)
        * 100.0
        / previous_year_sales,
        2
    ) AS growth_percentage
FROM sales_with_previous
ORDER BY year;

-- Create SQL views
-- yearly sales
CREATE VIEW IF NOT EXISTS yearly_sales AS
SELECT
    year,
    SUM(sales) AS total_sales
FROM sales
GROUP BY year;

-- regional
CREATE VIEW IF NOT EXISTS regional_sales AS
SELECT
    region,
    SUM(sales) AS total_sales
FROM sales
GROUP BY region;

-- category
CREATE VIEW IF NOT EXISTS category_sales AS
SELECT
    category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY category;

SELECT *
FROM yearly_sales;