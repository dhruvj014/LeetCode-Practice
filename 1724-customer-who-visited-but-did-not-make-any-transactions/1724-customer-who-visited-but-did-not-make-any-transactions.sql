# Write your MySQL query statement below
Select v.customer_id, Count(*) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id is Null
Group by v.customer_id