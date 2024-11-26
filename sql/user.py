import sqlite3


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register(self, db):
        try:
            db.insert("users", {
                "username": self.username,
                "password": self.password,
                "email": self.email
            })
            print("Реєстрація пройшла успішно!")
        except sqlite3.IntegrityError as e:
            print(f"Помилка реєстрації: {e}")

    @staticmethod
    def login(db, username, password):
        query = "SELECT * FROM users WHERE username=? AND password=?"
        user = db.fetch_one(query, (username, password))
        if user:
            print(f"Успішний вхід, користувач: {username}")
            return True
        else:
            print("Неправильні дані!")
            return False