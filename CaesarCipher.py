import re

def encrypt(plainText, offset):
    cipherText=""
    for letter in plainText:
        if letter.isalpha():
            cipherText = cipherText + chr(ord(letter) + offset)
        else:
            cipherText = cipherText + letter
    return cipherText

def decrypt(cipherText, offset):
    plainText=""
    for letter in cipherText:
        if letter.isalpha():
            plainText = plainText + chr(ord(letter) - offset)
        else:
            plainText = plainText + letter
    return plainText
    
def showMenu():
    while True:
        choice = input('Select Operation:\n1.)Encrypt\n2.)Decrypt\n3.)Exit\nChoice: ')
        if choice=="1":
            print(encrypt(input('Enter string to encrypt: '), int(input('Enter offset: '))))
        elif choice=="2":
            print(decrypt(input('Enter string to decrypt: '), int(input('Enter offset: '))))
        elif choice=="3":
            break
        else:
            print('Invalid choice')


if __name__ == "__main__":
    showMenu()