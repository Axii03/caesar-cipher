print("Welcome to Caesar Cipher Encrypter")
word=input("Enter your string to encrypt: ")
key=int(input("Enter the key: "))
letters=list(word.lower());
length=len(letters)
number=[0]*length
outputWord=['']*length
for i in range(0,length):
        number[i]=ord(letters[i])+key
        if number[i]>122:
            number[i]=number[i]-26
for x in range(0,length):
    outputWord[x]=chr(number[x])
encryptWord=''.join(outputWord)
print("Plain text: ", word)
print("Cipher text: ",encryptWord)
