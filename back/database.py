from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./PATTERNS.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Pattern(Base):
    __tablename__ = "patterns"

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

Base.metadata.create_all(bind=engine)

session = SessionLocal()

def delete(id: int):
    from os import delete as Del
    global session
    pattern = session.query(Pattern).get(id)
    Del(pattern.image)
    Del(pattern.file)
    session.delete(pattern)
    session.commit()
    return 200

def pattern(id: int):
    global session
    return session.query(Pattern).get(id)

def patterns_substring(substr: str):
    global session
    return session.query(Pattern).filter(Pattern.name.contains(substr)).all()

def patterns_favorite(fav: bool):
    global session
    return session.query(Pattern).filter(Pattern.favorite == fav).all()

def patterns_category(category: int):
    global session
    return session.query(Pattern).filter(Pattern.category == category).all()

def categories():
    global session
    return session.query(Category).all()

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
    return pattern

def create_category(name: str):
    global session
    category = Category(name = name)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category