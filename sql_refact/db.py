import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self, host="localhost", user="root", password="", db_name="project"):
        self.db_name = db_name
        self.connection = None
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        """Підключення до бази даних"""
        if not self.connection:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.db_name
                )
                print("Підключення до бази даних успішне.")
            except Error as e:
                print(f"Помилка підключення до бази даних: {e}")
        return self.connection

    def create_database_if_not_exists(self):
        """Створення бази даних, якщо її немає"""
        query = f"CREATE DATABASE IF NOT EXISTS {self.db_name}"
        self.execute(query)
        print(f"Базу даних '{self.db_name}' було створено або вона вже існує.")

    @property
    def cursor(self):
        return self.connect().cursor()

    def execute(self, query: str, params=()):
        cursor = self.cursor
        cursor.execute(query, params)
        if any(keyword in query.upper() for keyword in ("INSERT", "UPDATE", "DELETE")):
            self.connection.commit()
        return cursor

    def fetch_all(self, query: str, params=()):
        cursor = self.cursor
        cursor.execute(query, params)
        return cursor.fetchall()

    def fetch_one(self, query: str, params=()):
        cursor = self.cursor
        cursor.execute(query, params)
        return cursor.fetchone()

    def create_table(self, table_name: str, schema: dict):
        """Створення таблиці з унікальними значеннями для username та email"""
        columns = ", ".join(f"{col} {d_type}" for col, d_type in schema.items())
        query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {columns},
                UNIQUE (username),
                UNIQUE (email)
            )
        """
        self.execute(query)

    def insert(self, table_name: str, data: dict):
        """Вставка нових даних до таблиці"""
        columns = ",".join(data.keys())
        questions = ",".join("%s" for _ in data)
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({questions})"
        self.execute(query, values)

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def check_duplicates(self, username, email):
        """Перевірка на дублікати для username та email"""
        query = "SELECT * FROM users WHERE username=%s OR email=%s"
        result = self.fetch_one(query, (username, email))
        if result:
            if result[1] == username:
                print(f"Логін '{username}' вже існує.")
            if result[3] == email:
                print(f"Email '{email}' вже використовується.")
            return True
        return False

