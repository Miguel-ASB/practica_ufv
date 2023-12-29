import shutil
import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import List

from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class SALE_VideoGames(BaseModel):
    Rank: int
    Name: str
    Platform: str
    Year: int
    Genre: str
    Publisher: str
    NA_Sales: float
    EU_Sales: float
    JP_Sales: float
    Other_Sales: float
    Global_Sales: float

class Listado_Ventas_VG(BaseModel):
    JuegosVideo: List[SALE_VideoGames]

app = FastAPI(
    title="Servidor de datos",
    description="Datos de ventas de videojuegos",
    version="0.1.0",
)

@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('/home/mangel/repositorios/repos/practica_ufv/streamlit/pages/vgsales.csv',sep=',')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = Listado_Ventas_VG()
    listado.JuegosVideo = todosmisdatosdict
    return listado