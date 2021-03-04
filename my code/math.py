from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fibonacci/{n}")
def fibonacci(n: int, q: Optional[str] = None):
    ar=[0,1]
    if n<2:
        return ar[0]
    elif n==2:
        return ar[1]
    for i in range(2,n,1):
        ar+=[ar[i-1]+ar[i-2]]
    return {"item_id": ar[n-1], "q": q}

@app.get("/fectorial/{n}")
def fectorial(n: int, q: Optional[str] = None):
    if n<1:
        return 1
    return {"item_id":n*fectorial(n-1), "q": q}

