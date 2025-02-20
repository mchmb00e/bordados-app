from fastapi.responses import FileResponse
import database

# Return pattern from database
def pattern(id: int):
    return database.pattern(id=id)

# Return image pattern from database
def pattern_preview(id: int):
    return FileResponse(pattern(id=id).image)

# Return list of patterns contains substring
def substring(substr: str):
    return database.patterns_substring(substr)

# Return list of favorite patterns
def favorite(fav: bool):
    return database.patterns_favorite(favorite)

# Return list of patterns with same category
def category(id: int):
    return database.patterns_category(id)

# Delete a pattern with the files
def delete(id: int):
    return database.delete(id = id)

# Return list of all categories
def categories(sort: bool = False):
    if sort:
        return database.categories()
    else:
        return database.categories()