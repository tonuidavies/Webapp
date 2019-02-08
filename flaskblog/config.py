import os


class Config:
    SECRET_KEY = 'zyuytdsrrhdcythgxhgchvt'
    SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tonuidavies@gmail.com'
    MAIL_PASSWORD = 'headmaster00'
