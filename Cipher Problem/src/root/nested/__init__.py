import StringIO
import sys
from cipherGrid import *
from cipherText import *
from decryptText import *


grid = cipherGrid.cipherGrid()
grid.printCipher()
printable = raw_input("Would you like to print the stages? (Y/N)")
if printable == "y":
    printable = True

    
stringText = raw_input("Please enter your message:")
text = cipherText()

if(text.encryptText(stringText, grid)) == True:
    if (printable == True):
            encrypted = text.printCipher(1)
            print("First Pass Cipher using the Grid: " + encrypted)
    keyword = raw_input("Message Accepted. Please enter a keyword:")
    if (text.parseKeyword(keyword)) == True:
        print ("Keyword Accepted. Your encrypted message is below.")
        if (printable == True):
            encrypted = text.printCipher(2)
            print("Second Pass Cipher using the Keyword: " + encrypted)
        else: 
            encrypted = text.printCipher(2)
            print(encrypted)
        raw_input("\nPress enter to decrypt.")
    else:
        print ("There is an error with your keyword")
        sys.exit()
else:
    print ("There is an error with your message")
    sys.exit()

decryption = decryptText()
if (printable):
    print(decryption.decrypt(grid, keyword, encrypted))
