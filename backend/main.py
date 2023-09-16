from fastapi import FastAPI, Form, Request
import sys
import os
from typing import Annotated, List

from autovalores import calcular_autovalor
from eclineales import calcular_gauss

sys.path.append(os.path.dirname(__file__))


app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/ecuacion-lineal", description="Resuelve un sistema de ecuaciones lineales predefinido utilizando el método de Gauss.")
async def solucionar_eclineal(random: bool = False):
    """
    :param random: solicita que se generaren datos aleatorios.
    """

    matriz = [
        [1, 1, -1],
        [0, 1, 3],
        [-1, 0, -2],
    ]

    vector = [9, 3, 2]

    matriz_reducida, vector_reducida, incognitas = calcular_gauss(matriz, vector)

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


@app.post("/ecuacion-lineal", description="Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss")
async def solucionar_eclineal_del_usuario(request: Request):
    """
    :param request: Representa el request.
    """
        
    # Debemos interpretar los parámetros del request
    data = await request.json()
    matriz = data["matriz"]
    vector = data["vector"]
    matriz_reducida, vector_reducida, incognitas = calcular_gauss(matriz, vector)

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


@app.get("/autovalores", description="Encuentra los autovalores de una matriz dada.")
async def solucionar_autovalores(random: bool = False):
    """
    :param random: solicita que se generaren datos aleatorios.
    """
    matriz = [
        [3.556, -1.778, 0],
        [-1.778, 3.556, -1.778],
        [0, -1.778, 3.556],
    ]

    solucion = calcular_autovalor(matriz)

    return {
        "problema": {
            "matriz": matriz,
        },
        "solucion": {
            "autovalor": solucion,
        }
    }


@app.post("/autovalores", description="Encuentra los autovalores de una matriz.")
async def solucionar_autovalores_del_usuario(request: Request):
    """
    :param request: Representa el request.
    """
        
    # Debemos interpretar los parámetros del request
    data = await request.json()
    matriz = data["matriz"]
    solucion = calcular_autovalor(matriz)

    return {
        "problema": {
            "matriz": matriz,
        },
        "solucion": {
            "autovalor": solucion,
        }
    }
