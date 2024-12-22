from pyembroidery import read_pes, write_png
from os.path import exists

def render(file: str, id: int):
    pattern = read_pes(file)
    export = f'RENDER/{str(id)}.PES'
    if exists(export):
        print("Ya existe")
        return export
    else:
        print("No existe")
        write_png(pattern, export)
        return export
        
