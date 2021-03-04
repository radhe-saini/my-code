from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fibonacci/{length}")
def fibonacci(length: int, q: Optional[str] = None):
    fibonacci_searis=[0,1]
    if length<2:
        return fibonacci_searis[0]
    elif length==2:
        return fibonacci_searis[1]
    for index in range(2,length,1):
        fibonacci_searis+=[fibonacci_searis[index-1]+ar[index-2]]
    return {"fibonacci item": fibonacci_searis[length-1], "q": q}

@app.get("/factorial/{number}")
def factorial(number: int, q: Optional[str] = None):
    if number<=1:
        return 1
    return {"result factorial":number*factorial(number-1), "q": q}

