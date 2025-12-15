SELECT 
    c.name AS category_name, 
    COUNT(d.document_id) AS doc_count
FROM categories c
JOIN documents d ON d.category_id = c.category_id
WHERE d.created_at BETWEEN '2024-01-01' AND '2025-12-31'
GROUP BY c.name
ORDER BY doc_count DESC;