SELECT 
    c.name, 
    MAX(d.created_at) AS last_update_date
FROM categories c
JOIN documents d ON d.category_id = c.category_id
WHERE d.title LIKE '%5%'
GROUP BY c.name;