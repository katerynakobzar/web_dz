class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register(self, db):
        """Реєстрація користувача з перевіркою на дублікати"""
        if not db.check_duplicates(self.username, self.email):
            try:
                db.insert("users", {
                    "username": self.username,
                    "password": self.password,
                    "email": self.email
                })
                print("Реєстрація пройшла успішно!")
            except mysql.connector.IntegrityError as e:
                print(f"Помилка реєстрації: {e}")

    @staticmethod
    def login(db, username, password):
        """Вхід користувача за логіном та паролем"""
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        user = db.fetch_one(query, (username, password))
        if user:
            print(f"Успішний вхід, користувач: {username}")
            return True
        else:
            print("Неправильні дані!")
            return False