from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./PATTERNS.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Modelo: Representación de una tabla en SQLite
class Pattern(Base):
    __tablename__ = "patterns"  # Nombre de la tabla

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(Integer, nullable=False)
    favorite = Column(Boolean, default=False)
    file = Column(String, nullable=True)
    image = Column(String, nullable=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, onupdate=func.now())

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

session = SessionLocal()

# Funciones para interactuar con la base de datos
def create_pattern(name: str, category: int, favorite: bool, file: str, image: str):
    global session
    pattern = Pattern(
        name = name,
        category = category,
        favorite = favorite,
        file = file,
        image = image
    )
    session.add(pattern)
    session.commit()
    session.refresh(pattern)
    return pattern.id

def create_category(name: str):
    global session
    category = Category(name=name)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category.id

def all_category():
    global session
    return session.query(Category).all()

def pattern_filter_category(category_id: int):
    global session
    return session.query(Pattern).filter(Pattern.category == category_id).all()

def pattern_get_image(pattern_id: int):
    return session.get(Pattern, pattern_id).image

def favorites():
    global session
    return session.query(Pattern).filter(Pattern.favorite == True).all()

def contains(substring: str):
    global session
    return session.query(Pattern).filter(Pattern.name.contains(substring)).all()

def close():
    global session
    session.close()
    return True
