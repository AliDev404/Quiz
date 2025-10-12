
score=0
wrong=[]


def mcq_input(question,options):
	print(f"\033[91m{question}\033[0m","❓")
	for i in options:
		print(i)
	while True:
		user_answer=input("Choose (A/B/C/D):\n").strip().upper()
		if user_answer in ['A','B','C','D']:
			return user_answer
		else:
			print("\a !!Wrong Input!!")


def mcq_check(question,options,user_answer,answer):
	global score, wrong
	if user_answer==answer[0]:
		score+=1
		print("Correct! ✅\n")
	else:
		wrong.append([question,options,user_answer,answer])
		print(f"\a\033[92m{answer}\033[0m\n")
	return score,wrong

