import StringIO
from cipherGrid import *
from cipherText import *


grid = cipherGrid.cipherGrid()
grid.printCipher()
stringText = raw_input("Please enter your message:")
text = cipherText()

if(text.encryptText(stringText, grid)) == True:
    keyword = raw_input("Message Accepted. Please enter a keyword:")
    if (text.parseKeyword(keyword)) == True:
        print ("Keyword Accepted. Your encrypted message is below.")
        text.printCipher(2)
        raw_input("\nPress enter to decrypt.")
    else:
        print ("There is an error with your keyword")
else:
    print ("There is an error with your message")

