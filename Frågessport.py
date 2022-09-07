while True:
    score=0
    name = (input("What is your name? "))
    print("Hello",name,"and welcome to this breaking bad quiz.")
    print("This quiz has 4 questions with 5 points for each answer, so now lets see how much you know Mr.white and his story.")
    print("Lets get started!")
    print("A. He loves money\nB. He wants to buy a new car\nC. He is dying of cancer")
    firstQ=input("Why did walter start cooking meth?").capitalize()
    if firstQ == "C":
        score +=5
    else:print( "False")

    print("A. Los pollos hermanos\nB. Los angeles burgers \nC. Gustavo burgers")
    secondQ=input("What was gustavo frings restaurant call?").capitalize()
    if secondQ=="A":
        score += 5
    else:print( "False")

    print( "Half way done!")
    print("A. Ricin\nB. Botox\nC. Polonium 210\nD. Lily of the valley")
    thirdQ=input("What did walter use to poison Brock?").capitalize()
    if thirdQ=="D":
        score += 5
    else:print("Come on",name,"I know you can do better than this")

    print("Last be not least")
    print("A. Royce\nB. louis\nC. Flynn")
    fourthQ=input("What was the name of walter's son?").capitalize()
    if fourthQ=="C":
        score += 5
    else:print("You sould rewatch the show!")

    print("Thank you for participating in this quiz you can find your results down below.")
    print("Mr/Ms",name,"you have scored",score,"out of 20")

    again=str(input("Do you want to play again, type yes or no "))
    if again != "yes":
        break