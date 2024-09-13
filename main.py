from fastapi import FastAPI #importa la clase fastapi de la libreria fastapi
from fastapi.responses import HTMLResponse #importa la clase HTMLResponse de la libreria fastapi
from movies_list import movies_list
app = FastAPI() #crea una instancia de la clase fastapi
app.title = "Mi primera aplicacion de peliculas y Analisis de Datos"
app.version = "0.0.1"
@app.get('/', tags=['Home']) #definiendo una ruta
def message():# definimos una funcion de la ruta
    return  HTMLResponse('<h1>Hola mundo</h1>') #retorna un objeto de la clase HTMLResponse

@app.get('/movies', tags=['Movies']) #definiendo una ruta
def movies():# definimos una funcion de la ruta
    return  movies_list

@app.get('/movies/{id}', tags=['Movies']) #app get consultar por id
def get_movie(id:int):# definimos una funcion de la ruta
    for item in movies_list:
        if item['id'] == id:
            return item
    return[]