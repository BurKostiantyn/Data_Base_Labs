INSERT INTO categories (name, description)
SELECT 
    'Auto_Category_' || i, 
    'Generated description ' || md5(random()::text)
FROM generate_series(1, 10) AS i;

WITH range_values AS (
    SELECT min(category_id) as min_id, max(category_id) as max_id FROM categories
)
INSERT INTO documents (title, category_id, created_at, content_path)
SELECT
    'Auto_Doc_' || md5(random()::text),
    floor(random() * (r.max_id - r.min_id + 1) + r.min_id)::int, 
	NOW() - (random() * interval '365 days'),
    '/var/www/uploads/file_' || i || '.pdf'
FROM generate_series(1, 100000) AS i, range_values r;
