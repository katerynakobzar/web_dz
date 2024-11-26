users_schema = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "username": "TEXT UNIQUE",
    "password": "TEXT",
    "email": "TEXT UNIQUE"
}