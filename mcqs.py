import json
from settings import settings


subject="subjects/test_sub"

with open(f"{subject}/mcqs.json", "r") as file:
    questions = json.load(file)
    total=0
    for question_i in questions:
        total+=1
        question=question_i["q"]
        options=question_i["options"]
        user_answer=settings.mcq_input(question,options)
        score, wrong=settings.mcq_check(question,options,user_answer,question_i["answer"])
        

print(f"Score: {score}/{total}")
if wrong:
    print(wrong)
