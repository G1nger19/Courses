import random
num = random.randint(0,101)

while True:
    answer=input("Input number: ")
    if not answer or answer == "exit":
        break
    
    if not answer.isdigit():
        print("input correct number")
        continue
    
    user_answer = int(answer)

    if user_answer>num:
        print("Your answer more")
    elif user_answer<num:
        print("Your answer less")
    else:
        print("YOHOO")
        break