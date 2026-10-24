
-- Query 1: Total item sales value
SELECT
    ROUND(SUM(price), 2) AS total_item_sales
FROM order_items;

-- Query 2: Top 10 orders by item sales
SELECT
    order_id,
    ROUND(SUM(price), 2) AS order_item_sales
FROM order_items
GROUP BY order_id
ORDER BY order_item_sales DESC
LIMIT 10;

-- Query 3: Monthly item sales for delivered orders
SELECT
    STRFTIME(
        CAST(o.order_purchase_timestamp AS TIMESTAMP),
        '%Y-%m'
    ) AS order_month,
    ROUND(SUM(i.price), 2) AS monthly_item_sales
FROM orders AS o
INNER JOIN order_items AS i
    ON o.order_id = i.order_id
WHERE o.order_status = 'delivered'
GROUP BY order_month
ORDER BY order_month;
