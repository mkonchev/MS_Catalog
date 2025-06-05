from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker, declarative_base
from app.models.Category import Category as CategoryEnum

# Подключение к SQLite (файл создастся автоматически)
SQLALCHEMY_DATABASE_URL = "sqlite:///./catalog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False}
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DBCatalogItem(Base):
    __tablename__ = "catalog_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(Enum(CategoryEnum))
    price = Column(Integer)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
