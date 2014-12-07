import random
import sys
class cipherGrid:
    
    global gridData
    global gridChars
    gridData = {"AA":"A"}
    gridChars = ["A"]
    global counter
    
    def __init__ (self):
        for i in range(66,102,1):
            if i > 90:
                randomData = str(i - 91)
            else:
                randomData =  str(unichr(i))
            gridChars.insert(0, randomData)
        self.shuffle()  
        self.createGrid()
    
    def printCipher(self):
        print ("  A  B  C  D  E  F")
        for i in range(65,71,1):
            sys.stdout.write(str(unichr(i)) + " ")
            for j in range(65,71,1):
                printData = gridData[(str(unichr(i)) + str(unichr(j)))]
                sys.stdout.write(printData + "  ")
            print("")   
                        
    def createGrid(self):
        counter=(len(gridChars))-1
        for i in range(65,71,1):
            for j in range(65,71,1):
                storeData = gridChars[counter]
                if (storeData == "10"):
                    storeData = "1"
                gridData[(str(unichr(i)) + str(unichr(j)))] = storeData
                counter = counter - 1
                
    def getItem(self, index): 
        return gridData.get(index)
    
    def searchItem(self, searchTerm):
        for i in range(65,71,1):
            for j in range(65,71,1):
                if gridData[(str(unichr(i)) + str(unichr(j)))] == searchTerm:
                    return (str(unichr(i)) + str(unichr(j)))
                      
    def shuffle(self):
        a=len(gridChars)
        b=a-1
        for d in range(b,0,-1):
            e=random.randint(0,d)
            if e == d:
                continue
            gridChars[d],gridChars[e]=gridChars[e],gridChars[d]
            
    def getCipher(self, textString):
        txtLength = len(textString)
        textString.split()
        global encodedMsg
        encodedMsg = ""
        for i in range(0, txtLength, 1):
            if textString[i] != " ":
                encodedMsg = encodedMsg + (self.searchItem(textString[i]))
        return encodedMsg
        
        
        
        