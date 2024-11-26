from db import DB
from user import User
import config


def main():
    db_client = DB()

    db_client.create_table("users", config.users_schema)

    while True:
        print("\nВиберіть опцію:")
        print("1 - Зареєструватися")
        print("2 - Увійти")
        print("3 - Вийти")

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
            print("Вихід з програми.")
            db_client.close()
            break

        else:
            print("Невірний вибір! Спробуйте ще раз.")


main()