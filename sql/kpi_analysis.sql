
-- Query 1: Sales KPI summary
SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,

    COUNT(DISTINCT CASE
        WHEN o.order_status = 'delivered'
        THEN o.order_id
    END) AS delivered_orders,

    ROUND(SUM(CASE
        WHEN o.order_status = 'delivered'
        THEN i.price
        ELSE 0
    END), 2) AS delivered_item_sales,

    ROUND(
        SUM(CASE
            WHEN o.order_status = 'delivered'
            THEN i.price
            ELSE 0
        END)
        /
        NULLIF(
            COUNT(DISTINCT CASE
                WHEN o.order_status = 'delivered'
                THEN o.order_id
            END), 0
        ),
        2
    ) AS avg_item_sales_per_delivered_order

FROM orders AS o
LEFT JOIN order_items AS i
    ON o.order_id = i.order_id;
