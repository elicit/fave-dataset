from pydantic import BaseModel
import json

# Models

class Paper(BaseModel):
    authors: list[str]
    summary: str
    title: str

class Sample(BaseModel):
    papers: list[Paper]
    query: str

with open('paper_dataset.json') as f:
    raw_data = json.load(f)
    data = [Sample.model_validate(d) for d in raw_data]

print("First query: ", data[0].query)
print("First paper of first query: ", data[0].papers[0].title)