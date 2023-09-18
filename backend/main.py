from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import random as rng
from typing import Annotated, List

from autovalores import calcular_autovalor
from interpolacion import lagrange_interpolation
from vectores import generar_matriz, generar_vector
from eclineales import calcular_gauss

sys.path.append(os.path.dirname(__file__))


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    if random:
        n = rng.randint(2, 6)
        matriz = generar_matriz(n)
        vector = generar_vector(n)

    matriz_reducida, vector_reducida, incognitas = calcular_gauss(
        matriz, vector)

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
    matriz_reducida, vector_reducida, incognitas = calcular_gauss(
        matriz, vector)

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

    if random:
        a = rng.randint(2, 6)
        b = rng.randint(2, 6)
        matriz = generar_matriz(a, b)

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


@app.get("/interpolacion", description="Realiza la interpolación de un punto en una matriz dada.")
async def solucionar_interpolacion(random: bool = False):
    """
    :param random: solicita que se generaren datos aleatorios.
    """
    x = [0.0, 1.0, 2.0, 3.0]
    y = [1.0, 2.0, 4.0, 8.0]

    # Valor en el cual se desea estimar y
    x0 = 1.5

    if random:
        n = rng.randint(2, 10)
        x = generar_vector(n)
        y = generar_vector(n)
        x0 = rng.randint(min(x), max(x))

    y0 = lagrange_interpolation(x, y, x0)

    return {
        "problema": {
            "x": x,
            "y": y,
            "x0": x0,
        },
        "solucion": {
            "y0": y0,
        }
    }


@app.post("/interpolacion", description="Realiza la interpolación de un punto en una matriz.")
async def solucionar_interpolacion_del_usuario(request: Request):
    """
    :param request: Representa el request.
    """

    # Debemos interpretar los parámetros del request
    data = await request.json()

    x = data["x"]
    y = data["y"]
    x0 = data["x0"]

    y0 = lagrange_interpolation(x, y, x0)

    return {
        "problema": {
            "x": x,
            "y": y,
            "x0": x0,
        },
        "solucion": {
            "y0": y0,
        }
    }
