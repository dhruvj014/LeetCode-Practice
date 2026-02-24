# Write your MySQL query statement below
SELECT round(
    SUM(order_date = customer_pref_delivery_date)/COUNT(*) * 100,2) AS immediate_percentage
FROM (
    select d.customer_id, d.order_Date, d.customer_pref_delivery_date
    FROM Delivery d
    JOIN (
        select customer_id,
        MIN(order_date) as first_order_date
        FROM Delivery
        Group By Customer_id
    ) AS first_orders
    ON d.customer_id = first_orders.customer_id
    AND d.order_date = first_orders.first_order_date
) AS sub