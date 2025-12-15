-- 1. Додаємо категорії
INSERT INTO categories (name, description) VALUES
('Накази', 'Офіційні розпорядження керівництва'),
('Заяви', 'Звернення співробітників'),
('Звіти', 'Щомісячні звіти про виконання робіт');

-- 2. Додаємо користувачів
INSERT INTO users (full_name, email, position) VALUES
('Іванов Іван', 'ivanov@mail.com', 'Менеджер'),
('Петров Петро', 'petrov@mail.com', 'Розробник'),
('Сидорова Анна', 'anna@mail.com', 'Бухгалтер');

-- 3. Додаємо документи (вже прив'язуємо до категорій)
INSERT INTO documents (title, category_id, content_path) VALUES
('Наказ про преміювання', 1, '/docs/orders/2025_001.pdf'),
('Заява на відпустку', 2, '/docs/applications/petrov_vac.pdf'),
('Річний звіт 2024', 3, '/docs/reports/year_2024.docx');

-- 4. Надаємо доступу (хто що бачить)
INSERT INTO doc_access (user_id, document_id, access_level) VALUES
(1, 1, 'edit'),   -- Іванов може редагувати Наказ
(2, 1, 'read'),   -- Петров може тільки читати Наказ
(3, 3, 'edit');   -- Сидорова редагує Звіт