SELECT
product_name, 
SUM(quantity*price) AS total_revenue
FROM sales
GROUP BY product_name;