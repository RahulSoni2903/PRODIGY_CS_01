def Encryption(plaintext,key):
    n=len(plaintext)
    Encrypted_password=""
    for i in range(0,n):
        if plaintext[i] >= 'a' and plaintext[i] <= 'z':
            Encrypted_password += chr(((ord(plaintext[i]) + key - 97) % 26 )+ 97)
        if plaintext[i] >= 'A' and plaintext[i] <= 'Z':
            Encrypted_password += chr(((ord(plaintext[i]) + key - 65) % 26 )+ 65)
    print("ciphertext:",Encrypted_password)
def Decryption(ciphertext,key):
    
    n=len(ciphertext)
    Decrypted_password=""
    for i in range(0,n):
        if ciphertext[i] >= 'a' and ciphertext[i] <= 'z':
            Decrypted_password += chr(122-(((122-(ord(ciphertext[i]) - key )) % 26 )+1)+1)
        if ciphertext[i] >= 'A' and ciphertext[i] <= 'Z':
             Decrypted_password += chr(90-(((90-(ord(ciphertext[i]) - key )) % 26 )+1)+1)
    print("plaintext:",Decrypted_password)


print("this is rahul")
print("This is encryption code")

plaintext=input("enter your plain text in this")
print(plaintext)
key=int(input("enter your key in this"))
print(key)
Encryption(plaintext,key)
ciphertext=input("enter your cipher text in this")
print(ciphertext)
key=int(input("enter your key value in this"))
print(key)
Decryption(ciphertext,key)