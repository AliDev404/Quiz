import json

score=0
wrong=[]
subject="subjects/test_sub"

with open(f"{subject}/mcqs.json", "r") as file:
    questions = json.load(file)
    total=0
    for i,question in enumerate(questions):
        total+=1
        print(f"{question["q"]}\n")
        for option in question["options"]:
            print(option)
        user_answer=input("Choose (A/B/C):\n").strip().upper()
        if user_answer==question["answer"]:
            score+=1
        else:
            wrong.append([i,question,option,user_answer,question["answer"]])


print(f"Score: {score}/{total}")

if wrong:
    print(wrong)