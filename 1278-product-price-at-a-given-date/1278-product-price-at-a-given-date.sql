# Write your MySQL query statement below
SELECT p.product_id, 
        COALESCE(latest.new_price,10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM Products
) p
LEFT JOIN (
    SELECT product_id, new_price
    FROM (
        SELECT *,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as rn
        FROM Products
        WHERE change_date <= '2019-08-16'
        ) t
    WHERE rn = 1
) latest
ON p.product_id = latest.product_id