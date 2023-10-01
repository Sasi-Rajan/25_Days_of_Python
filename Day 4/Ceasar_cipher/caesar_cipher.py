from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(text,shift,direction):
    start=True
    while start:
        cipher=""
        if shift > 26:
            shift=shift%26
        for letter in text:
            if letter in alphabet:
                old_pos=alphabet.index(letter)
                if direction == "encode":
                    new_pos=old_pos+shift
                if direction == "decode":
                    new_pos=old_pos-shift
                new_val=alphabet[new_pos]
                cipher=cipher+new_val
            else:
                cipher=cipher+letter
        print(f"Your {direction}d message is {cipher}")
        again=input("Do you want to start the program again y/n ")
        if again == "y":
            start=True
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
        else:
            start=False

ceasar(text,shift,direction)
