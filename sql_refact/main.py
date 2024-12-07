from db import DB
from user import User
from site_registration import SiteRegistration

def main():
    db_client = DB(host="localhost", user="root", password="", db_name="project")

    db_client.create_database_if_not_exists()

    db_client.connect()

    # Створення таблиць
    users_schema = {
        "id": "INT AUTO_INCREMENT PRIMARY KEY",
        "username": "VARCHAR(255) NOT NULL",
        "password": "VARCHAR(255) NOT NULL",
        "email": "VARCHAR(255) NOT NULL"
    }

    site_registration_schema = {
        "id": "INT AUTO_INCREMENT PRIMARY KEY",
        "user_id": "INT",
        "site_name": "VARCHAR(255) NOT NULL",
        "login": "VARCHAR(255) NOT NULL",
        "password": "VARCHAR(255) NOT NULL",
        "login_method": "VARCHAR(50) NOT NULL",  # Google, Facebook, Apple, тощо
        "FOREIGN KEY(user_id)": "REFERENCES users(id)"
    }

    db_client.create_table("users", users_schema)
    db_client.create_table("site_registrations", site_registration_schema)

    while True:
        print("\nВиберіть опцію:")
        print("1 - Зареєструватися")
        print("2 - Увійти")
        print("3 - Додати сайт до реєстрацій")
        print("4 - Переглянути зареєстровані сайти")
        print("5 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            email = input("Введіть email: ")

            new_user = User(username=username, password=password, email=email)
            new_user.register(db_client)

        elif choice == "2":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")

            User.login(db_client, username, password)

        elif choice == "3":
            user_id = int(input("Введіть ваш ID користувача: "))
            site_name = input("Введіть назву сайту: ")
            login = input("Введіть логін на сайті: ")
            password = input("Введіть пароль на сайті: ")
            login_method = input("Введіть метод входу (Google, Facebook, Apple): ")

            site_registration = SiteRegistration(db_client, user_id, site_name, login, password, login_method)
            site_registration.register_site()

        elif choice == "4":
            user_id = int(input("Введіть ваш ID користувача: "))
            SiteRegistration.get_user_sites(db_client, user_id)

        elif choice == "5":
            print("Вихід з програми.")
            db_client.close()
            break

        else:
            print("Невірний вибір! Спробуйте ще раз.")

main()
