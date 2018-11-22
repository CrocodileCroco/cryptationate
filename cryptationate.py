startchoice = input("Crypter ou décrypter (E/D) : ")
if startchoice == "E" :
    encrytext = input("Texte a crypter : ")
    encrytedtext = ''
    for letter in encrytext :
        encrytedtext += chr(ord(letter) + 3)
    print("---")
    print(encrytedtext)
    print("---") 
if startchoice == "D" :
    decrytext = input("Texte a decrypter : ")
    decrytedtext = ''
    for letter in decrytext :
        decrytedtext += chr(ord(letter) - 3)
    print("---")
    print(decrytedtext)
    print("---") 
input("Appuyez sur un bouton pour fermer le programme")