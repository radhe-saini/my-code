from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/length/{sample_string}")
def length(sample_string: str, q: Optional[str] = None):
    index=0
    try:
        while sample_string[index]:
            index+=1
    except IndexErrorr:
        return {"length of string": index, "q": q}

@app.get("/gen_string/{no_of_char}")
def gen_string(no_of_char: int, q: Optional[str] = None):
    result_string=''
    for _ in range(no_of_char):
        result_string+=input()
    return {"generated string":result_string, "q": q}

