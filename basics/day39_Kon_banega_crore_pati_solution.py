# kai log list ko array boltey hein , kyunki C , javascript main sab array heen boltey hein , but technically galat heen hein , kyunki python mein app nahi bolsaktey
# agar koi baat kar raha hein object ki to samaj jana vo set ki baat kar raha hein
# Format is Question ,5-Options , and the index position of the correct option


questions = [
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4],
    ["Which Language was used to create fb?","Python","French","Javascript","Php","None", 4]

]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
i = 0
for i in range(0,len(questions)):
        question = questions[i]
        print(f"Question for Rs . {levels[i]} ")
        print(f"a. {question[1]}          b. {question[2]}")
        print(f"a. {question[3]}          b. {question[4]}")
        reply = int(input("Enter your answer (1-4) ro 0 to Quit "))
        if (reply == 0):
            money = levels[i-1]
            break
        if (reply == question[-1]):
            print(f"\n\nCorrect answer, you havve won Rs. {levels[i]}")
            if(i==4):
                money = 10000
            elif(i==9):
                money = 320000
            elif(i==14):
                money = 10000000
        else:
            print("Wrong answer!!!!")
            break