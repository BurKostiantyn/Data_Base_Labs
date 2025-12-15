from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        err = self.model.connect()
        if err:
            self.view.show_message(err)
            return

        while True:
            choice = self.view.show_menu()

            if choice == '1':
                cats = self.model.get_categories()
                self.view.show_list("Список категорій (ID, Назва, Опис)", cats)

            elif choice == '2':
                docs = self.model.get_documents()
                self.view.show_list("Список документів (ID, Назва, ID Категорії)", docs)

            # --- КАТЕГОРІЇ ---
            elif choice == '3':
                # Додати категорію
                name = self.view.get_input("Введіть назву категорії: ")
                desc = self.view.get_input("Введіть опис категорії: ")
                msg = self.model.add_category(name, desc)
                self.view.show_message(msg)

            elif choice == '4':
                # Видалити категорію
                cat_id = self.view.get_input("Введіть ID категорії для видалення: ")
                msg = self.model.delete_category(cat_id)
                self.view.show_message(msg)

            elif choice == '5':
                # Редагувати категорію
                cat_id = self.view.get_input("Введіть ID категорії для редагування: ")
                new_name = self.view.get_input("Введіть НОВУ назву: ")
                new_desc = self.view.get_input("Введіть НОВИЙ опис: ")
                msg = self.model.update_category(cat_id, new_name, new_desc)
                self.view.show_message(msg)

            # --- ДОКУМЕНТИ ---
            elif choice == '6':
                # Додати документ
                title = self.view.get_input("Введіть назву документа: ")
                cat_id = self.view.get_input("Введіть ID категорії: ")
                msg = self.model.add_document(title, cat_id)
                self.view.show_message(msg)

            elif choice == '7':
                # Видалити документ
                doc_id = self.view.get_input("Введіть ID документа для видалення: ")
                msg = self.model.delete_document(doc_id)
                self.view.show_message(msg)

            elif choice == '8':
                # Редагувати документ
                doc_id = self.view.get_input("Введіть ID документа для редагування: ")
                new_title = self.view.get_input("Введіть НОВУ назву документа: ")
                new_cat_id = self.view.get_input("Введіть НОВИЙ ID категорії: ")
                msg = self.model.update_document(doc_id, new_title, new_cat_id)
                self.view.show_message(msg)

            elif choice == '0':
                break
            else:
                self.view.show_message("Невірний вибір.")