from fastapi import FastAPI
from fastapi.responses import FileResponse
from model import session, Pattern

app = FastAPI()

@app.get("/pattern/favorites")
def favorites():
    return session.query(Pattern).filter(Pattern.favorite == True).all()

@app.get("/pattern/{id}")
def pattern_id(id: int):
    return session.query(Pattern).get(id)

@app.get("/pattern/contains/{text}")
def pattern_contains(text: str):
    return session.query(Pattern).filter(Pattern.name.ilike(f"%{text}%")).all()

@app.get("/pattern/favorite/{id}")
def pattern_favorite(id: int):
    pattern = session.query(Pattern).get(id)
    pattern.favorite = not pattern.favorite
    session.commit()
    return 200

@app.get("/pattern/rename/{new_name}")
def rename(new_name: str, id: int):
    pattern = session.query(Pattern).get(id)
    pattern.name = new_name
    session.commit()
    return 200

@app.get("/export/{id}")
def export(id: int):
    from shutil import copy
    from os import listdir
    pattern = session.query(Pattern).get(id)
    copy(pattern.file, f"/media/mchmb00e/{listdir("/media/mchmb00e")[0]}")
    return 200

@app.get("/media/")
def media():
    from os import listdir
    return listdir(r"/media/mchmb00e")

@app.get("/preview/{id}")
def preview(id: int):
    return FileResponse(session.query(Pattern).get(id).preview)
