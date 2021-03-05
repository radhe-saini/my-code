from typing import Optional
from fastapi import FastAPI
import pytest
import uvicorn
"""math module"""
APP = FastAPI(debug=True)

@APP.get("/")
def read_root():
    """
    localhost output"""
    return {"Hello": "World"}


@APP.get("/fibonacci/{length}")
def fibonacci(length: int, q: Optional[str] = None):
    """fibonacci module
    """
    fibonacci_searis = [0, 1]
    if length < 2:
        return fibonacci_searis[0]
    if length == 2:
        return fibonacci_searis[1]
    for index in range(2, length, 1):
        fibonacci_searis += [fibonacci_searis[index-1]+fibonacci_searis[index-2]]
    return {"fibonacci item": fibonacci_searis[length-1], "q": q}




@APP.get("/factorial/{number}")
def factorial(number: int, q: Optional[str] = None):
    #factorial module
    
    def fact(number):
        if number <= 1:
            return 1
        return number*fact(number-1)

    res = fact(number)
    return {"result factorial":res, "q": q}

if __name__ == ("__main__"):
    uvicorn.run(APP, host="127.0.0.1", port=8000)
