"""string module
"""
from typing import Optional
import uvicorn
from fastapi import FastAPI

APP = FastAPI(debug=True)

@APP.get("/")
def read_root():
    """
    localhost output"""
    return {"Hello": "World"}



@APP.get("/length/{sample_string}")
async def length(sample_string: str):
    """length function"""
    index = 0
    try:
        while sample_string[index]:
            index += 1
    except IndexError:
        return {"length of string": index}


@APP.get("/gen_string/{no_of_char}")
async def gen_string(no_of_char: int):
    """
    2 nd end point - string generation"""
    result_string = ""
    for _ in range(no_of_char):
        result_string += input()
    return {"generated string":result_string}


if __name__ == ('__main__'):
    uvicorn.run(APP, host="127.0.0.1", port = 3000)

