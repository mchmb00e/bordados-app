# fastapi dev main.py
from fastapi import FastAPI, UploadFile, File, Form
import get
import os
from shutil import copy, copyfileobj
from pyembroidery import write_png, read_pes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permitir React Vite en desarrollo
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)
base_media = r"/media/mchmb00e"
media_usb = os.listdir(base_media)
media_select = None

# GET
@app.get("/patterns/preview/{id}")
async def patterns_preview(id: int):
    return get.pattern_preview(id=id)

@app.get("/patterns/{id}")
async def pattern(id: int):
    return get.pattern(id = id)

@app.get("/patterns/")
async def filter(
    substring: str = None,
    favorite: bool = None,
    category: int = None):
    if substring is not None:
        return get.substring(substring)
    elif favorite is not None:
        return get.favorite(favorite)
    elif category is not None:
        return get.category(category)
    else:
        return 400
 
@app.get("/patterns/delete/{id}")
async def delete(id: int):
    return get.delete(id=id)

@app.get("/categories/")
async def categories(sort: bool = False):
    return get.categories(sort = sort)

@app.get("/patterns/export/{id}")
async def patterns_export(id: int):
    global base_media, media_select
    pattern = get.pattern(id=id)
    copy(pattern.file, f"{base_media}/{media_select}")


@app.get("/media/")
async def media():
    return media_usb

@app.get("/media/listdir/")
async def media_listdir():
    global media_select, base_media
    return os.listdir(f"{base_media}/{media_select}")

@app.get("/media/select/{name}")
async def select(name: str):
    global base_media
    global media_select
    media_select = name
    return os.listdir(f"{base_media}/{media_select}")


@app.get("/media/delete/{name}")
async def media_delete(name: str):
    global media_select, base_media
    os.delete(f"{base_media}/{media_select}/{name}")





@app.post("/upload/pattern/")
async def upload_pattern(
    name: str = Form(...),
    category: int = Form(...),
    favorite: bool = Form(...),
    file: UploadFile = File(...)
):
    
    from database import create_pattern

    # Definir la ruta donde se guardará el archivo
    file_path = os.path.join("BORDADOS", file.filename)

    image_path = os.path.join("PREVIEW", file.filename[:-4] + ".png")

    write_png(read_pes(file), image_path)
    
    # Guardar el archivo en el servidor
    with open(file_path, "wb") as buffer:
        copyfileobj(file.file, buffer)

    create_pattern(name=name, category=category, favorite=favorite, file=file_path, image=image_path)

    return {
        "message": "Pattern uploaded successfully",
        "name": name,
        "category": category,
        "favorite": favorite,
        "file_path": file_path,
    }

@app.get("/upload/category/{name}")
async def upload_category(name: str):
    from database import create_category
    create_category(name)