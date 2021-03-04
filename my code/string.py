from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/length/{s}")
def length(s: str, q: Optional[str] = None):
    i=0
    while s[i]:
        i+=1
    return {"item_id": i, "q": q}

@app.get("/gen_string/{n}")
def gen_string(n: int, q: Optional[str] = None):
    s=''
    for i in range(n):
        s+=input()
    return {"item_id":s, "q": q}

