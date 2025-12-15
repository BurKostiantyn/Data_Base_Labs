class View:
    def show_menu(self):
        print("\n=== СИСТЕМА УПРАВЛІННЯ ДОКУМЕНТАМИ ===")
        print("1. Показати всі категорії")
        print("2. Показати всі документи")
        print("---------------------------")
        print("--- КАТЕГОРІЇ ---")
        print("3. ДОДАТИ категорію")
        print("4. ВИДАЛИТИ категорію")
        print("5. РЕДАГУВАТИ категорію")
        print("---------------------------")
        print("--- ДОКУМЕНТИ ---")
        print("6. ДОДАТИ документ")
        print("7. ВИДАЛИТИ документ")
        print("8. РЕДАГУВАТИ документ")
        print("---------------------------")
        print("0. Вихід")
        return input("Оберіть дію: ")

    def show_message(self, message):
        print(f"\n>>> {message}")

    def show_list(self, title, data):
        print(f"\n--- {title} ---")
        if not data:
            print("Список порожній.")
        else:
            for row in data:
                print(row)

    def get_input(self, text):
        return input(text)