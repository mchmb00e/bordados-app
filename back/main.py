from fastapi import FastAPI
from fastapi.responses import FileResponse
import database as db
from pydantic import BaseModel

app = FastAPI()

@app.get("/get/list/category")
def list_category():
    return db.all_category()

@app.get("/get/list/pattern")
def list_pattern(category: int = None, favorite: bool = False, substring: str = None):
    if category is not None:
        return db.pattern_filter_category(category_id = category)
    elif favorite:
        return db.favorites()
    elif substring is not None:
        return db.contains(substring = substring)

@app.get("/get/preview/{id}")
def preview(id: int):
    return FileResponse(db.pattern_get_image(pattern_id = id))