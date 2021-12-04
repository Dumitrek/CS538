import string
import random

alphabet = string.ascii_letters
otp = list(alphabet)

def genKey(keyLength):
    key = ''.join(random.choice(alphabet) for x in range(keyLength))
    return key

def encryption(plaintext, key):
    ciphertext=''
    for index, char in enumerate(plaintext):
        charIndex = alphabet.index(char)
        keyIndex = otp.index(key[index])
        cipherChar = (keyIndex + charIndex) % len(otp)
        ciphertext += alphabet[cipherChar]
    return ciphertext

def decryption(ciphertext, key):
    plaintext=''
    for index, char in enumerate(ciphertext):
        charIndex = alphabet.index(ciphertext[0])
        keyIndex = otp.index(key[0])
        cipherChar = (charIndex - keyIndex) % len(otp)
        char = alphabet[cipherChar]
        plaintext = char + decryption(ciphertext[1:], key[1:])
    return plaintext
    
def main():
    plaintext = input('Enter plaintext: \n')
    keyLength = int(input('How long do you want your key to be: \n'))
    key = genKey(keyLength)
    ciphertext = encryption(plaintext, key)
    print('Ciphertext: \n' +ciphertext)
    plaintext = decryption(ciphertext, key)
    print("Plaintext: \n" +plaintext)
    key = ''
    print ('Key: ' +key)
    exit (0)

if __name__ == '__main__':
    main()
