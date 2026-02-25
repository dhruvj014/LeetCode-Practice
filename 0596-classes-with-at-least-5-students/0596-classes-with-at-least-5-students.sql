# Write your MySQL query statement below
SELECT c.class
FROM Courses c
JOIN (
    SELECT class, Count(student) as cnt
    FROM Courses
    GROUP BY class
) as f
ON c.class = f.class
AND f.cnt > 4
GROUP BY c.class