import json

score=0
wrong=[]
with open("questions.json", "r") as file:
    questions = json.load(file)
    for i,question in enumerate(questions):
        print(f"{question["q"]}\n")
        for option in question["options"]:
            print(option)
        user_answer=input("Choose (A/B/C):").strip().upper()
        if user_answer==question["answer"]:
            score+=1
        else:
            wrong.append((i,question,option,user_answer,question["answer"]))


print(score)
if wrong:

    print(wrong)