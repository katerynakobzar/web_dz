class SiteRegistration:
    def __init__(self, db, user_id, site_name, login, password, login_method):
        self.db = db
        self.user_id = user_id
        self.site_name = site_name
        self.login = login
        self.password = password
        self.login_method = login_method

    def register_site(self):
        """Реєстрація на сайті для користувача"""
        existing_site = self.db.fetch_one(
            "SELECT * FROM site_registrations WHERE user_id=%s AND site_name=%s AND login_method=%s",
            (self.user_id, self.site_name, self.login_method)
        )
        if existing_site:
            print(f"Ви вже зареєстровані на сайті {self.site_name} через {self.login_method}.")
        else:
            self.db.insert("site_registrations", {
                "user_id": self.user_id,
                "site_name": self.site_name,
                "login": self.login,
                "password": self.password,
                "login_method": self.login_method
            })
            print(f"Інформація про реєстрацію на сайті {self.site_name} успішно додана.")

    @staticmethod
    def get_user_sites(db, user_id):
        """Отримати всі сайти, на яких зареєстрований користувач"""
        query = "SELECT * FROM site_registrations WHERE user_id=%s"
        sites = db.fetch_all(query, (user_id,))
        if sites:
            print("Ви зареєстровані на наступних сайтах:")
            for site in sites:
                print(f"Сайт: {site[2]}, Логін: {site[3]}, Вид входу: {site[5]}")
        else:
            print("Ви не зареєстровані на жодному сайті.")

