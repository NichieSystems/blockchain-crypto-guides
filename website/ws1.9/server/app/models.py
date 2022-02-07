from flask_login import UserMixin

class User(UserMixin):
    __tablename__ = "users"