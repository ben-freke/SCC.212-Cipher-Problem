import cipherGrid
class cipherText:
    global message
    global textValid
    def encryptText(self, textString, grid):
        textValid = True
        txtLength = len(textString)
        textString.split()
        textString = textString.upper()
        for i in range(0, txtLength, 1):
            if ((ord(textString[i])) < 64) | ((ord(textString[i])) > 91):
                if (ord(textString[i]) != 32):
                    textValid = False
                    return False
                else:
                    continue
        if (textValid):   
            print (textString)
            print(grid.getCipher(textString))
            return True
        
    