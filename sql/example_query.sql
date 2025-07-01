-- Example query for data analysis
SELECT 
    column1,
    column2,
    COUNT(*) AS record_count,
    AVG(numeric_column) AS avg_value
FROM 
    your_table
WHERE 
    date_column >= '2024-01-01'
    AND status = 'active'
GROUP BY 
    column1, 
    column2
ORDER BY 
    record_count DESC
LIMIT 100;