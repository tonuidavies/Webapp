import os


class Config:
    SECRET_KEY = 'sdhgfhjbafkhbwekfguewjbfukh'#os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'#os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tonuidavies@gmail.com'#os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'headmaster00'#os.environ.get('MAIL_PASSWORD')
