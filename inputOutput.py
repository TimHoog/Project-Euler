import eulerChallenges
import answerSheet


def askinput():
    import answerSheet
    print("What Project Euler answer do we want to calculate?")
    while True:
        userinput = input("I want to calculate Euler challenge nr.: ")
        if userinput.isdigit():
            userinput = int(userinput)
            if userinput in answerSheet.eulerChallengeList:
                eulername = answerSheet.eulerChallengeList[userinput]
                eulername = eulername[2]
                print(f"Let's calculate Euler challenge #{str(userinput)}: {eulername}!")
                return userinput
            else:
                print("I have yet to solve this Euler challenge \n")
        else:
            print("Please enter an integer number")


def runfunction(userinput):
    import time
    challengeresult = []
    t0 = time.time()
    challenge = answerSheet.eulerChallengeList[userinput]
    challengeresult.append(str(challenge[0]()))
    challengeresult.append(challenge[1])
    t1 = time.time()
    challengeresult.append(t1-t0)
    return challengeresult


def checkresult(answerlist):
    if answerlist[0] == answerlist[1]:
        x = "Great succes! :)"
    else:
        x = "Better luck next time :("
    print("We are looking for the answer: " + str(answerlist[1]))
    print("We calculated the following:   " + str(answerlist[0]))
    print("calculating took " + str(answerlist[2]) + " seconds.")
    print(x)


