import psycopg
from config import db_config


class Model:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg.connect(**db_config, autocommit=True)
        except Exception as e:
            return f"Помилка підключення до БД: {e}"

    # --- Робота з таблицею CATEGORIES (Батьківська) ---
    def get_categories(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT category_id, name, description FROM categories ORDER BY category_id")
                return cursor.fetchall()
        except Exception as e:
            return []

    def delete_category(self, cat_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM categories WHERE category_id = %s", (cat_id,))
                if cursor.rowcount == 0:
                    return "Помилка: Категорії з таким ID не існує."
            return f"Категорію {cat_id} успішно видалено."

        except psycopg.errors.ForeignKeyViolation:
            return "ПОМИЛКА (Foreign Key): Неможливо видалити категорію, бо в ній існують документи!"

        except Exception as e:
            return f"Системна помилка: {e}"

    def add_category(self, name, description):
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO categories (name, description) VALUES (%s, %s)"
                cursor.execute(query, (name, description))
            return "Категорію успішно створено."
        except Exception as e:
            return f"Помилка при створенні категорії: {e}"

    def update_category(self, cat_id, new_name, new_desc):
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE categories SET name = %s, description = %s WHERE category_id = %s"
                cursor.execute(query, (new_name, new_desc, cat_id))
                if cursor.rowcount == 0:
                    return "Помилка: Категорії з таким ID не знайдено."
            return f"Категорію {cat_id} успішно оновлено."
        except Exception as e:
            return f"Помилка оновлення категорії: {e}"

    # --- Робота з таблицею DOCUMENTS (Дочірня) ---
    def get_documents(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT document_id, title, category_id FROM documents ORDER BY document_id")
                return cursor.fetchall()
        except Exception as e:
            return []

    def add_document(self, title, category_id):
        try:
            with self.connection.cursor() as cursor:
                query = """
                        INSERT INTO documents (title, category_id, created_at, content_path)
                        VALUES (%s, %s, CURRENT_DATE, 'default/path') \
                        """
                cursor.execute(query, (title, category_id))
            return "Документ успішно додано."

        except psycopg.errors.ForeignKeyViolation:
            return f"ПОМИЛКА (Foreign Key): Категорії з ID {category_id} не існує. Спочатку створіть категорію."

        except Exception as e:
            return f"Інша помилка: {e}"

    def delete_document(self, doc_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM documents WHERE document_id = %s", (doc_id,))
                if cursor.rowcount == 0:
                    return "Помилка: Документа з таким ID не знайдено."
            return f"Документ {doc_id} успішно видалено."
        except psycopg.errors.ForeignKeyViolation:
            return "Помилка: Неможливо видалити документ, бо існують записи про доступ до нього (doc_access)."
        except Exception as e:
            return f"Помилка видалення: {e}"

    def update_document(self, doc_id, new_title, new_cat_id):
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE documents SET title = %s, category_id = %s WHERE document_id = %s"
                cursor.execute(query, (new_title, new_cat_id, doc_id))
                if cursor.rowcount == 0:
                    return "Помилка: Документа з таким ID не знайдено."
            return f"Документ {doc_id} успішно оновлено."
        except psycopg.errors.ForeignKeyViolation:
            return f"Помилка (FK): Категорії з ID {new_cat_id} не існує. Неможливо перенести документ."
        except Exception as e:
            return f"Помилка оновлення документа: {e}"