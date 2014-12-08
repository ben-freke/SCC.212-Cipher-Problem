import sys
import cipherGrid
class cipherText:
    global message
    global textValid
    
 
    
    def encryptText(self, textString, grid):
        global firstCipher
        textValid = True
        txtLength = len(textString)
        textString.split()
        textString = textString.upper()
        for i in range(0, txtLength, 1):
            if ((ord(textString[i])) < 64) | ((ord(textString[i])) > 91):
                if ((ord(textString[i])) < 47) | ((ord(textString[i])) > 58):
                    if (ord(textString[i]) != 32):
                        textValid = False
                        return False
                    else:
                        continue
                else:
                    continue
        if (textValid):   
            firstCipher = grid.getCipher(textString)
            return True

    def parseKeyword(self, keyWord):
        length1 = len(firstCipher)
        counter1 = 0
        noColumns = len(keyWord)
        if (length1 % noColumns) == 0:
            noRows = length1/noColumns
            keyWord.split()
            firstCipher.split()
            global secondPassCipher
            for i in range(0, noRows, 1):
                for j in range(0, noColumns, 1):
                    if (i == 0) & (j == 0):
                        secondPassCipher = [(keyWord[j], i, firstCipher[counter1])]
                    else:
                        secondPassCipher = secondPassCipher + [(keyWord[j], i, firstCipher[counter1])]
                
                    counter1 = counter1 + 1
           
            secondPassCipher.sort(cmp=None, key=None, reverse=False)
            secondPassCipher = ([x[2] for x in secondPassCipher])
            
          
                
            
            return True
        else:
            return False
         
    def printCipher(self, passNo):
        cipher = ""
        if passNo == 1:
            for i in range(0, len(firstCipher),1):
                cipher = cipher + firstCipher[i]
        if passNo == 2:
            for i in range(0, len(secondPassCipher),1):
                cipher = cipher + secondPassCipher[i]
        return cipher       
        
        