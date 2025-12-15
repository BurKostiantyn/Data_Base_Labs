SELECT 
    d.document_id, 
    d.title, 
    c.name AS category_name, 
    d.created_at
FROM documents d
JOIN categories c ON d.category_id = c.category_id
WHERE d.title LIKE '%Auto%'
  AND c.category_id BETWEEN 1 AND 5
ORDER BY d.document_id DESC
LIMIT 50;