import requests

def caesarCipher(word, shift):
    encryptedStr = ""
    for i in range (len(word)):
        letter = word[i]
        #chr() function returns the letter as unicode
        #ord() function returns unicode -> integer
        if letter == " ":
            encryptedStr += " "
            #print(encryptedStr)
        elif (letter.isupper()):
            encryptedStr += chr((ord(letter) + shift-65) % 26 + 65)
            #print(encryptedStr)
        else:
            encryptedStr += chr((ord(letter) + shift-97) % 26 + 97)
            #print(encryptedStr)
    return encryptedStr
def deCaesarCipher(word, shift):
    encryptedStr = ""
    for i in range (len(word)):
        letter = word[i]
        if letter == " ":
            encryptedStr += " "
        elif (letter.isupper()):
            encryptedStr += chr((ord(letter) - shift-65) % 26 + 65)
        else:
            encryptedStr += chr((ord(letter) - shift-97) % 26 + 97)
    return encryptedStr

def bruteForceCaeser(encryptedMessage):
    # 1000 Most common words
    url = 'https://raw.githubusercontent.com/powerlanguage/word-lists/master/1000-most-common-words.txt'
    response = requests.get(url)
    fileOfWords = response.text
    for shift in range (26):
        decryptedStr = ""
        for i in range (len(encryptedMessage)):
            letter = encryptedMessage[i]
            if letter == " ":
                decryptedStr += " "
            elif (letter.isupper()):
                decryptedStr += chr((ord(letter) - shift-65) % 26 + 65)
            else:
                decryptedStr += chr((ord(letter) - shift-97) % 26 + 97)
            #print (decryptedStr)
        for dWord in decryptedStr.split():
            for common_word in fileOfWords.split('\n'):
                if dWord in common_word.split():
                    return decryptedStr

print(bruteForceCaeser("whvw rq zrugv"))