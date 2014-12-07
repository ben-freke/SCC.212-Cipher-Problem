import StringIO
from cipherGrid import *
from cipherText import *


grid = cipherGrid.cipherGrid()
grid.printCipher()
stringText = raw_input("Please enter your message:")
text = cipherText()

if(text.encryptText(stringText, grid)) == True:
    print ("Message Accepted")
else:
    print ("There is an error with your message")

