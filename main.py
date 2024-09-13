from fastapi import FastAPI #importa la clase fastapi de la libreria fastapi

app = FastAPI() #crea una instancia de la clase fastapi
app.title = "Mi primera aplicacion de peliculas y Analisis de Datos"
app.version = "0.0.1"
@app.get('/', tags=['Home']) #definiendo una ruta
def message():# definimos una funcion de la ruta
    return  'Hello World' #devolvemos un diccionario
