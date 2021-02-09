class Caesar():
    def __init__(self, text):
        self.text = text

    def encryption(self):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        encrypted_text = ""

        for char in text:
            for alpha in alphabets:
                if char == alpha:
                    encrypted_text += alphabets[(alphabets.index(alpha) + 3) % 26]
            if char not in alphabets:
                encrypted_text += char
        print("Encrypted Text: ", encrypted_text)

    def decryption(self):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        decrypted_text = ""

        for char in text:
            for alpha in alphabets:
                if char == alpha:
                    decrypted_text += alphabets[(alphabets.index(alpha) - 3) % 26]
            if char not in alphabets:
                decrypted_text += char
        print("Decrypted Text: ", decrypted_text)


while True:
    choice = input(
        "\n========================CAESAR-CYPHER========================\n1. Encryption\n2. Decryption\n3. Exit\nChoose operation: ")
    if choice == str(1):
        text = input("Enter the text to Encrypt: ")
        obj = Caesar(text)
        obj.encryption()
    elif choice == str(2):
        text = input("Enter the text to Decrypt: ")
        obj = Caesar(text)
        obj.decryption()
    elif choice == str(3):
        print("Bye")
        break
    else:
        print("Please enter a valid choice.")
