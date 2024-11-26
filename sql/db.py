import sqlite3


class DB:
    def __init__(self, db_name="project.db") -> None:
        self.db_name = db_name
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_name)

        self.connection.row_factory = sqlite3.Row  # возвращает строки как словари
        return self.connection

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
        res = cursor.execute(query, params)
        return res.fetchall()

    def fetch_one(self, query: str, params=()):
        cursor = self.cursor
        cursor.execute(query, params)
        return cursor.fetchone()

    def create_table(self, table_name: str, schema: dict):
        columns = ", ".join(f"{col} {d_type}" for col, d_type in schema.items())
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute(query)

    def insert(self, table_name: str, data: dict):
        columns = ",".join(data.keys())
        questions = ",".join("?" for _ in data)
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({questions})"
        self.execute(query, values)

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None