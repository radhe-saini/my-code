"""math module
"""
from typing import Optional

from fastapi import FastAPI

APP = FastAPI()



@APP.get("/")
def read_root():
    """
    localhost output"""
    return {"Hello": "World"}



@APP.get("/fibonacci/{length}")
def fibonacci(length: int, q_u: Optional[str] = None):
    """fibonacci module
    """
    fibonacci_searis = [0, 1]
    if length < 2:
        return fibonacci_searis[0]
    if length == 2:
        return fibonacci_searis[1]
    for index in range(2, length, 1):
        fibonacci_searis += [fibonacci_searis[index-1]+fibonacci_searis[index-2]]
    return {"fibonacci item": fibonacci_searis[length-1], "q": q_u}


@APP.get("/factorial/{number}")
def factorial(number: int, q_u: Optional[str] = None):
    """factorial module
    """
    if number <= 1:
        return 1
    return {"result factorial":number*factorial(number-1), "q": q_u}
