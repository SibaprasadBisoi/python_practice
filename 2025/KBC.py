contestent = str(input("Enter you name:"))
print(f"\nHello {contestent}, Welcome to KBC !\n\n")
print(" Yeh raha aapka pehla question, TV screen par. Dhyan se jawab dijiyega.\n\n What is the capital of Arunachal Pradesh ?")
print("\nA. Meghalaya     B. Damandiu     C. Ittanagar    D. Ladakh\n\n Please select your answer from above options A, B, C or D")
Answers = []
Answer1 = str(input("Enter your answer: "))
Answer1=Answer1.capitalize()
print(f"Your answer is : {Answer1}")
Answers.append(Answer1)
if Answer1 == "C":
    print("Sahi jawab! Aap 10000 jitgaye, congratulations!\n")
elif Answer1== "A" or "B" or "D" or "a" or "b" or "d":
    print("Galat Jawab, app ke pass aur ek mauka hai aage khelne ka.")
else:
    print("Please select your answer from above options A, B, C or D")


print(" Yeh raha aapka dusra question, TV screen par. Dhyan se jawab dijiyega.\n\n How many startes are there in india ?")
list = ["A. 27", "B. 28", "C. 29", "D. 30"]
print(list)
Answer2 = str(input("Enter your answer: "))
Answer2=Answer2.capitalize()
print(f"Your answer is : {Answer2}")
Answers.append(Answer2)
print(Answers)
if Answer2 == "B":
    print("Sahi jawab! Aap 100000 jitgaye, congratulations!")

    print(" Yeh raha aapka teesra question, TV screen par. Dhyan se jawab dijiyega.\n\n Who has designed indian flag ?")
    list = ["A. Pingali Venkayya", "B. Venkaya Naidu", "C. Venktesh Iyer", "D. Rabindra nath tagore"]
    print(list)
    Answer3 = str(input("Enter your answer: ")) 
    Answer3=Answer3.capitalize()
    print(f"Your answer is : {Answer3}")
    Answers.append(Answer3)
    print(Answers)
    if Answer3 == "A":
        print("Sahi jawab! Aap 100000 jitgaye, congratulations!")
    elif Answer3 == "B" or "C" or "D" or "B" or "c" or "d":
        print("Galat Jawab !")
        if Answers[0] == "C"  and  Answers[1] == "B" and Answers[2] == "A":
            print("Aap aage khel sakte hai.")
        else:
            print("Aap aage nahi khel sakte hai, Kshyama chahuga me. Aap ka safar yahan tak raha!")
    
    else:
        print("Please select your answer from above options A, B, C or D")

    print("Aaj yehin pe samapt karenge, next episode pe milenge! Namaskar")
elif Answer2 == "A" or "C" or "D" or "a" or "c" or "d":
    print("Galat Jawab !")
    if Answers[0] == "C"  and  Answers[1] == "B" :
        print("Aap aage khel sakte hai.")
    else:
        print("Aap aage nahi khel sakte hai, Kshyama chahuga me. Aap ka safar yahan tak raha!")
    
else:
    print("Please select your answer from above options A, B, C or D")

# print(" Yeh raha aapka teesra question, TV screen par. Dhyan se jawab dijiyega.\n\n Who has designed indian flag ?")
# list = ["A. Pingali Venkayya", "B. Venkaya Naidu", "C. Venktesh Iyer", "D. Rabindra nath tagore"]
# print(list)
# Answer3 = str(input("Enter your answer: "))
# Answer2.capitalize()
# print(f"Your answer is : {Answer3}")
# Answers.append(Answer3)
# print(Answers)
# if Answer3 == "A":
#     print("Sahi jawab! Aap 100000 jitgaye, congratulations!")
# elif Answer3 == "B" or "C" or "D" or "B" or "c" or "d":
#     print("Galat Jawab !")
#     if Answers[0] == "C"  and  Answers[1] == "B" and Answers[2] == "A":
#         print("Aap aage khel sakte hai.")
#     else:
#         print("Aap aage nahi khel sakte hai, Kshyama chahuga me. Aap ka safar yahan tak raha!")
    
# else:
#     print("Please select your answer from above options A, B, C or D")

# print("Aaj yehin pe samapt karenge, next episode pe milenge! Namaskar")
