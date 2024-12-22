from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///bordados.db", echo=True)

Base = declarative_base()

class Bordado(Base):
    __tablename__ = 'bordados'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    ubicacion = Column(String)
    favorito = Column(Boolean)
    categoria = Column(Integer)
    imagen = Column(String, nullable=True)

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def insertar_bordado(nombre: str, ubicacion: str, favorito: bool, categoria: int, imagen=None):
    global session
    if imagen is not None:
        bordado = Bordado(nombre=nombre, ubicacion=ubicacion, favorito=favorito, categoria=categoria, imagen=imagen)
    else:
        bordado = Bordado(nombre=nombre, ubicacion=ubicacion, favorito=favorito, categoria=categoria)
    session.add(bordado)
    session.commit()

def insertar_categoria(nombre: str):
    global session
    categoria = Categoria(nombre=nombre)
    session.add(categoria)
    session.commit()

def obtener_nombres():
    global session
    nombres = session.query(Bordado.nombre).all()
    return nombres

def ubicacion_por_nombre(nombre: str):
    global session
    nombres = session.query(Bordado).filter(Bordado.nombre == nombre).all()
    return nombres[0].ubicacion

def id_por_nombre(nombre: str):
    global session
    ids = session.query(Bordado).filter(Bordado.nombre == nombre).all()
    return ids[0].id