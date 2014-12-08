import cipherGrid
class decryptText:
    def decrypt(self, grid, keyword, encrytped):
        rows = len(encrytped)
        columns = len(keyword)
        rows = rows/columns
        keyword.split()
        keywordArray = sorted(keyword)
        encrytped.split()
        counter1 = 0
        global secondPassCipher
        for i in range(0, columns, 1):
            for j in range(0, rows,1):
                if (i == 0) & (j == 0):
                    secondPassCipher = [(keywordArray[i], j, encrytped[counter1])]
                else:
                    secondPassCipher = secondPassCipher + [(keywordArray[i], j, encrytped[counter1])]
                counter1 = counter1+1
        
        firstPassCipher = ""
        counter1 = 0
        counter2 = 0
        counter3 = 0
        firstPassCipher = sorted(secondPassCipher, key=lambda i: i[1])
        global firstCipher
        firstCipher = ""
        while True:
            counterReset = False
            if ((firstPassCipher[counter1][0]) == keyword[counter2]): 
                firstCipher = firstCipher + firstPassCipher[counter1][2]
                if counter2 == columns-1:
                    counter2 = 0
                    counter3 = counter3 + columns
                else:
                    counter2 = counter2 + 1
                counter1 = counter3
                counterReset = True
            if (counterReset == False):
                counter1 = counter1 + 1
            if counter3 == (rows*columns):
                break;
        
        originalText = ""
        firstCipher.split()
        for i in range(0, len(firstCipher), 2):
            originalText = originalText + (grid.getItem(firstCipher[i]+firstCipher[i+1]))
        
        return originalText
        
        
       
      
            
            
            
            