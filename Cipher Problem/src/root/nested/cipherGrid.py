from random import randrange
from objc._objc import NULL
class cipherGrid:
    
    global gridData
    global gridChars
    gridChars = ["A"]
    gridData = [[0,0,0]]
    global counter
    
    def __init__ (self):
        for i in range(66,102,1):
            if i > 90:
                randomData = i - 91
            else:
                randomData =  str(unichr(i))
            gridChars.insert(0, randomData)
           

    def printCipher(self):
        for i in range(36, 0, -1):
            print gridChars[i]
            
    def createGrid(self):
        print "I am in Create Grid"
        
    def shuffleChars(self):
        for i from n - 1 downto 1 do
        j ← random integer with 0 ≤ j ≤ i
       exchange gridChars[j] and [i]    
    