from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Crear la base para los modelos
Base = declarative_base()

# Definir un modelo de ejemplo
class Pattern(Base):
    __tablename__ = "patterns"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    favorite = Column(Boolean, nullable=False, default=False)
    file = Column(String, unique=True, nullable=False)
    preview = Column(String, unique=True, nullable=False)

# Crear la conexión con SQLite
DATABASE_URL = "sqlite:///patterns.db"
engine = create_engine(DATABASE_URL, echo=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la BD
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()