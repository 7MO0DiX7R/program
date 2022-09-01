score=0
name = (input("What is your name? "))
print("Hello",name,"and welcome to this breaking bad quiz.")
print("This quiz has 4 questions with 5 points for each answer, so now lets see how much you now mr.white and his story.")
print("Lets get started!")
print("A. He loves money\nB. He wants to buy a new car\nC. He is dieing of cancer")
fristQ=input("Why did walter start cooking meth?")
if fristQ=="c".capitalize():
    score+= 5
else: print ("fel")
print("your score is",score)