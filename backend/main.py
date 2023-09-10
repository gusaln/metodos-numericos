import sys
import os
from typing import Annotated

from eclineales import gauss

sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/ecuacion-lineal")
async def eclineal():
    matriz = [
        [1, 1, -1],
        [0, 1, 3],
        [-1, 0, -2],
    ]

    vector = [9,3,2]

    matriz_reducida, vector_reducida, incognitas = gauss(matriz, vector)

    return {
        "problema": {
            "matriz": matriz,
            "vector": vector,
        },
        "solucion": {
            "matriz_reducida": matriz_reducida,
            "vector_reducida": vector_reducida,
            "soluciones": incognitas,
        }
    }

@app.post("/ecuacion-lineal")
async def solucionar_eclineal(matriz: Annotated[str, Form()], vector: Annotated[str, Form()]):
    matriz_reducida, vector_reducida, incognitas = gauss(matriz, vector)

    return {
        "problema": {
            "matriz": matriz,
            "vector": vector,
        },
        "solucion": {
            "matriz_reducida": matriz_reducida,
            "vector_reducida": vector_reducida,
            "soluciones": incognitas,
        }
    }