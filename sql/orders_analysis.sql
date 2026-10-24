
-- Query 1: Count all orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Query 2: Count orders by status
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- Query 3: Count orders by month
SELECT
    STRFTIME(
        CAST(order_purchase_timestamp AS TIMESTAMP),
        '%Y-%m'
    ) AS order_month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_month
ORDER BY order_month;
