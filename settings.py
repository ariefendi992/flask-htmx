from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SECRET_KEY = "ABCDBEFEG123"
