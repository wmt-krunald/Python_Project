from email.policy import default
import random

num_pass = int(input("\nEnter the Number of Password you want: "))
length = int(input("\nEnter the Length of your Password: "))
a = length - 6
c = a + a

if length < 8:
    print("\nYour Length should be greater then 8.")
else:
    s_char = "abcdefghijklmnopqrstuvwxyz"
    # print(random.choice(s_char))
    c_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sp_char = "~!@#$%^&*()_+-*/<>?/.[,]"
    n_char = "0123456789"
    all_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+-*/<>?/.[,]0123456789"

    def sm_ch():
        return random.choice(s_char)
    def cp_ch():
        return random.choice(c_char)
    def sp_ch():
        return random.choice(sp_char)
    def num_ch():
        return random.choice(n_char)
    def all_ch():
        return random.choice(all_ch)
    def err_han():
        return "Invalid Input"

    print('''
        1. small character
        2. Capital Character
        3. Special Character
        4. Number
        5. All Character
    ''')
    
    print("press 5 for all choices")
    print("press 3 for only 3 choices")
    print("press 2 for only 2 choices")
    print("press 1 for only 1 choice")

    choice_count = int(input("\nPlease tell how mant total choice you want!! : "))

    if choice_count == 5:
        for p in range(num_pass):
            passwords = ""
            for c in range(length):
                passwords += random.choice(all_char)
            print("\n",passwords)

    elif choice_count == 3:
        print("\nYou are an option that you need specific format fonts only.")
        print("\nPlease, Provide Your Choices..")
        choice1 = int(input("\nEnter Your Choice 1: "))
        choice2 = int(input("\nEnter Your Choice 2: "))
        choice3 = int(input("\nEnter Your Choice 3: "))

        mul_choice = {
            1: sm_ch,
            2: cp_ch,
            3: sp_ch,
            4: num_ch,
            5: all_ch
        }

        # out1 = mul_choice.get(choice1, err_han)()
        # # print(out1)

        # out2 = mul_choice.get(choice2, err_han)()
        # # print(out2)

        # out = out1 + out2
        # print(out)

        for p in range(num_pass):

            out1 = ""
            for c in range(a):  
                out1 += mul_choice.get(choice1, err_han)()
            # print("\n",out1)

            out2 = ""
            for c in range(a):  
                out2 += mul_choice.get(choice2, err_han)()
            # print("\n",out2)
            # print(out1 + out2)

            out3 = ""
            for c in range(length - c):  
                out2 += mul_choice.get(choice3, err_han)()
            # print("\n",out2)
            print(out1 + out2 + out3)

    elif choice_count == 2:
        print("\nYou are an option that you need specific format fonts only.")
        print("\nPlease, Provide Your Choices..")
        choice1 = int(input("\nEnter Your Choice 1: "))
        choice2 = int(input("\nEnter Your Choice 2: "))

        mul_choice = {
            1: sm_ch,
            2: cp_ch,
            3: sp_ch,
            4: num_ch,
            5: all_ch
        }

        # out1 = mul_choice.get(choice1, err_han)()
        # # print(out1)

        # out2 = mul_choice.get(choice2, err_han)()
        # # print(out2)

        # out = out1 + out2
        # print(out)

        for p in range(num_pass):

            out1 = ""
            for c in range(length - 4):  
                out1 += mul_choice.get(choice1, err_han)()
            # print("\n",out1)

            out2 = ""
            for c in range(4):  
                out2 += mul_choice.get(choice2, err_han)()
            # print("\n",out2)
            print(out1 + out2)

    elif choice_count == 1:
        print("\nYou are SELECT an option that you need specific format fonts only.")
        print("\nPlease, Provide Your Choice..")

        choice1 = int(input("\nEnter Your Choice 1: "))

        mul_choice = {
            1: sm_ch,
            2: cp_ch,
            3: sp_ch,
            4: num_ch,
            5: all_ch
        }

        for p in range(num_pass):
            passwords = ""
            for c in range(length):
                passwords += mul_choice.get(choice1, err_han)()
            print("\n",passwords)
    else:
        print("ERROR")


