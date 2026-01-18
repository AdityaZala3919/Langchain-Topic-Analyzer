from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from typing import Annotated

from pipeline import build_chains
from models import TopicRequest

app = FastAPI()
chains = build_chains()

@app.get("/")
def root():
    return RedirectResponse("/docs")

@app.post("/get/analyze")
def analyze_topic(input: Annotated[TopicRequest, Form()]):
    response = chains["final_chain"].invoke({"topic": input.topic})
    return response

@app.post("/get/summary")
def summary_function(input: str = Form()):
    response = chains["summary_chain"].invoke({"topic": input.topic})
    return response

@app.post("/get/keywords")
def keywords_function(input: str = Form()):
    response = chains["keywords_chain"].invoke({"topic": input.topic})
    return response

@app.post("/get/quiz")
def quiz_function(input: str = Form()):
    response = chains["quiz_chain"].invoke({"topic": input.topic})
    return response

@app.post("/get/difficulty")
def difficulty_function(input: str = Form()):
    response = chains["difficulty_chain"].invoke({"topic": input.topic})
    return response