from typing import Union

from fastapi import FastAPI

from quiz.schemas import Question

app = FastAPI()


@app.post("/quiz")
def read_root(item: Question):
    return {"Hello": item.questions_num}
