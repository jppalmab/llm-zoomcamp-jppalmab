#!wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/minsearch.py

import minsearch
import json

with open("./documents.json", "rt") as f:
    docs_raw = json.load(f)

# docs_raw

documents = []

for course_dict in docs_raw:
    for doc in course_dict["documents"]:
        doc["course"] = course_dict["course"]
        documents.append(doc)

documents[0]

index = minsearch.Index(
    text_fields=["question", "text", "section"],
    keyword_fields=["course"],
)

# SELECT * WHERE course = 'data-engineering-zoomcamp';


q = "the course has already started, can I still enroll?"

index.fit(documents)

index.search(q)

# ----------------------------------------------------------------------------------
# Example
# boost = {
#     "question": 3.0,
#     "section": 0.5,
# }

# results = index.search(
#     query=q,
#     filter_dict={"course": "data-engineering-zoomcamp"},
#     boost_dict=boost,
#     num_results=5)

# results

# ----------------------------------------------------------------------------------

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o", message=[{"role": "user", "content": q}]
)

response.choices[0].message[0].content
