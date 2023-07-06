from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT

# Создание URL-адреса базы данных MySQL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание движка SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создание класса сессии SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базового класса моделей SQLAlchemy
Base = declarative_base()

# Функция зависимости для получения экземпляра сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
