import random

def gusse_num(n):
    low = 1
    high = n
    feedback = ""

    while feedback != "c":

        if low != high: #check number is = or not
            gusse = random.randint(low, high) #generate every time random number bteween low & high
        else:
            gusse = high #or low bcuz low = high

        feedback = input(f"\nIs {gusse} is\n\ntoo High (H)?\tor\ntoo Low (L)?\tor\nCorrect(C)?\t").lower()

        if feedback == "h":
            high = gusse - 1 #if number is high then it will set high number to gusse - 1.
        elif feedback == "l":
            low = gusse + 1 #if number is low then it will set low numbedr to gusse + 1.

    print(f"\nYou have succesfully guss the number {gusse}.")
    print("You are a Winner!!!!!!!\n")

gusse_num(500)