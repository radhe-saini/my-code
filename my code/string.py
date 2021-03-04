"""string module
"""
from typing import Optional

from fastapi import FastAPI

APP = FastAPI()



@APP.get("/")
def read_root():
    """
    localhost output"""
    return {"Hello": "World"}



@APP.get("/length/{sample_string}")
def length(sample_string: str, q: Optional[str] = None):
    """length function"""
    index = 0
    try:
        while sample_string[index]:
            index += 1
    except IndexError:
        return {"length of string": index, "Q": q}


@APP.get("/gen_string/{no_of_char}")
def gen_string(no_of_char: int, q: Optional[str] = None):
    """
    2 nd end point - string generation"""
    result_string = ''
    for _ in range(no_of_char):
        result_string += input()
    return {"generated string":result_string, "q": q}
