-- 1. Створюємо таблицю категорій
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- 2. Створюємо таблицю користувачів
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(100),
    position VARCHAR(100)
);

-- 3. Створюємо таблицю документів (із прив'язкою до категорій)
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE,
    content_path VARCHAR(255),
    category_id INTEGER REFERENCES categories(category_id)
);

-- 4. Створюємо таблицю доступу (зв'язок N:M із атрибутом)
CREATE TABLE doc_access (
    access_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    document_id INTEGER REFERENCES documents(document_id),
    access_level VARCHAR(50)
);