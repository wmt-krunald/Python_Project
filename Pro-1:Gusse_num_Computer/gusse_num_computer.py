import random #This is random function


def gusse_num(n):

    random_number = random.randint(1, n) #Generate the random number
    gusse = 0

    while gusse != random_number:
        gusse = int(input(f"\nGusse the Number Between 1 to {n}: ")) #take the input from user.

        if gusse > random_number:
            print("\nSorry, Gusse again. It's too high.")
        elif gusse < random_number:
            print("\nSorry, Gusse again. It's too low.")

    print("\nHurreeyy, You are a winner!\n")
    print(f"You have correctly Gusse the number {gusse}.\n")

gusse_num(502)        
    