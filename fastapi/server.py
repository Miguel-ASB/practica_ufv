import shutil

import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import  List

from pydantic import BaseModel as PydanticBaseModel
class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True
class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class VideoGame(BaseModel):
    Platform: str
    Year_of_Release: str
    Genre: str
    Publisher: str
    NA_Sales: float
    EU_Sales: float
    JP_Sales: float
    Other_Sales: float
    Global_Sales: float
    Critic_Score: float
    Critic_Count: int
    User_Score: float
    User_Count: int
    Developer: str
    Rating: str

class ListadoVideoGames(BaseModel):
    video_games: List[VideoGame]

app = FastAPI(
    title="Servidor de datos",
    description="Servimos datos de videojuegos",
    version="0.1.0",
)

@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('./video_games_sales.csv', sep=',')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoVideoGames(video_games=todosmisdatosdict)
    return listado