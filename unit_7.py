n = "abcdefghijklmnopqrstuvwxyz"
def decision():
    while True:
        choice = input("press e to incode, d to decode or q to quit: ")
        if choice == "e":
            return encode()
        elif choice == "d":
            return decode()
        elif choice == "q":
            return quit()
        else:
            return decision()










def encode():
    string = input("please enter the text to be encoded: ")
    key = int(input("please enter the key (0-25): "))
    r = n[key:26] + n[0:key]
    print(string.index())
















def decode():
    string = input("please enter the text to be decoded: ")
    key = int(input("please enter the key (0-25): "))
    r = n[key:26] + n[0:key]





    






def quit():
    print("Thanks for playing")




decision()