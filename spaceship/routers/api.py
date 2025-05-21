from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.post('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/matrices')
def multiply() -> dict:
    a = np.random.rand(10, 10).tolist()
    b = np.random.rand(10, 10).tolist()
    product = (np.matmul(a, b)).tolist()
    return {"matrix_a": a, "matrix_b": b, "product": product}
