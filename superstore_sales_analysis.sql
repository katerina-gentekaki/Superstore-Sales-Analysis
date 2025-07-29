/*Business Question 1 – Total Sales by Region 
What is the total sales amount for each region?*/

SELECT SUM(sales) AS total_sales, region
FROM sales_analysis
GROUP BY region
ORDER BY total_sales DESC;

/*Business Question 2 – Total Sales by State
What is the total sales amount for each region?*/

SELECT SUM(sales) as total_sales, state 
FROM sales_analysis
GROuP BY state
ORDER BY total_sales DESC;

/*Business Question 3 – Total Profit by Product Category
Which product categories generated the highest total profit?*/


SELECT category, SUM(profit) AS total_profit
FROM sales_analysis
GROUP BY category
ORDER BY total_profit DESC; 

/*Business Question 4 – Revenue and Profit by Category
What is the What is the total revenue, total profit, and profit margin percentage for each product category?*/

SELECT 
  category,
  SUM(sales) AS revenue,
  SUM(profit) AS profit,
  ROUND(SUM(profit) / NULLIF(SUM(sales), 0) * 100, 2) AS profit_margin_percent
FROM sales_analysis
GROUP BY category;

/*Business Question 5 – Top 5 Products by Sales
Which products had the highest total sales?*/

SELECT product_name, SUM(sales) AS total_sales
FROM sales_analysis
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;

/*Business Question 6 – Monthly Sales Trend
How did sales vary across different months?*/

SELECT TO_CHAR(order_date, 'YYYY-MM') AS order_month, SUM(Sales) AS total_sales
FROM sales_analysis
GROUP BY order_month
ORDER BY order_month DESC;

/*Business Question 7 – Total Orders by Customer Segment¶
Which customer segment placed the most orders?*/

SELECT COUNT(*) as total_orders, segment
FROM sales_analysis
GROUP BY segment
ORDER BY total_orders;

/*Business Question 8 – Average Discount by Product Category
What is the average discount given per product category?*/

SELECT AVG(discount) as avg_discount,category 
FROM sales_analysis
GROUP BY category
ORDER BY avg_discount DESC;
