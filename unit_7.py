# written by oliver hamburger

# program encodes and decodes a given string

# string of alphabet
n = "abcdefghijklmnopqrstuvwxyz"


def decision():
    """function takes a decision and runs the apropriet function"""
    while True:
        choice = input("press e to incode, d to decode or q to quit: ")
        if choice == "e":
            return encode()
        elif choice == "d":
            return decode()
        elif choice == "q":
            return end()
        else:
            return decision()


def encode():
    """function takes a string and encodes it with the shifted alphabet made by the given key"""
    string = input("please enter the text to be encoded: ")
    key = int(input("please enter the key (0-25): "))
    r = n[key:26] + n[0:key]
    encoded = ""
    for x in string:
        encoded += r[n.index(x)]

    print(encoded)
    decision()


def decode():
    """function takes a string and decodes it with the shifted alphabet made by the given key"""
    string = input("please enter the text to be decoded: ")
    key = int(input("please enter the key (0-25): "))
    r = n[key:26] + n[0:key]
    decoded = ""
    for x in string:
        decoded += n[r.index(x)]

    print(decoded)
    decision()


def end():
    """function thanks user for playing and ends program"""
    print("Thanks for playing")


# function runs decision function to start program
def main():
    decision()


main()
