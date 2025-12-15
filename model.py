from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, text
from orm_models import Session, Category, Document


class Model:
    def __init__(self):
        self.session = None

    def connect(self):
        try:
            self.session = Session()
            self.session.execute(text("SELECT 1"))
            return None
        except Exception as e:
            return f"Помилка підключення до БД (ORM): {e}"

    # --- CATEGORIES ---
    def get_categories(self):
        try:
            categories = self.session.query(Category).order_by(Category.category_id).all()
            return [(c.category_id, c.name, c.description) for c in categories]
        except Exception as e:
            return []

    def add_category(self, name, description):
        try:
            new_cat = Category(name=name, description=description)
            self.session.add(new_cat)
            self.session.commit()
            return "Категорію успішно створено (ORM)."
        except Exception as e:
            self.session.rollback()
            return f"Помилка створення: {e}"

    def delete_category(self, cat_id):
        try:
            cat = self.session.get(Category, cat_id)
            if not cat:
                return "Помилка: Категорії з таким ID не існує."

            self.session.delete(cat)
            self.session.commit()
            return f"Категорію {cat_id} успішно видалено (ORM)."

        except IntegrityError:
            self.session.rollback()
            return "ПОМИЛКА (IntegrityError): Неможливо видалити категорію, бо в ній існують документи!"
        except Exception as e:
            self.session.rollback()
            return f"Системна помилка: {e}"

    def update_category(self, cat_id, new_name, new_desc):
        try:
            cat = self.session.get(Category, cat_id)
            if not cat:
                return "Помилка: Категорії не знайдено."

            cat.name = new_name
            cat.description = new_desc
            self.session.commit()
            return f"Категорію {cat_id} успішно оновлено (ORM)."
        except Exception as e:
            self.session.rollback()
            return f"Помилка оновлення: {e}"

    # --- DOCUMENTS ---
    def get_documents(self):
        try:
            docs = self.session.query(Document).order_by(Document.document_id).all()
            return [(d.document_id, d.title, d.category_id) for d in docs]
        except Exception as e:
            return []

    def add_document(self, title, category_id):
        try:
            new_doc = Document(
                title=title,
                category_id=category_id,
                created_at=func.current_date()
            )
            self.session.add(new_doc)
            self.session.commit()
            return "Документ успішно додано (ORM)."

        except IntegrityError:
            self.session.rollback()
            return f"ПОМИЛКА (IntegrityError): Категорії з ID {category_id} не існує."
        except Exception as e:
            self.session.rollback()
            return f"Помилка: {e}"

    def delete_document(self, doc_id):
        try:
            doc = self.session.get(Document, doc_id)
            if not doc:
                return "Помилка: Документ не знайдено."

            self.session.delete(doc)
            self.session.commit()
            return f"Документ {doc_id} успішно видалено (ORM)."
        except IntegrityError:
            self.session.rollback()
            return "Помилка: Неможливо видалити документ (зв'язки)."
        except Exception as e:
            self.session.rollback()
            return f"Помилка: {e}"

    def update_document(self, doc_id, new_title, new_cat_id):
        try:
            doc = self.session.get(Document, doc_id)
            if not doc:
                return "Помилка: Документ не знайдено."

            doc.title = new_title
            doc.category_id = new_cat_id
            self.session.commit()
            return f"Документ {doc_id} успішно оновлено."
        except IntegrityError:
            self.session.rollback()
            return f"Помилка (IntegrityError): Категорії з ID {new_cat_id} не існує."
        except Exception as e:
            self.session.rollback()
            return f"Помилка: {e}"