from string import ascii_uppercase as up

class Vigenere:
    def __init__(self) -> None:
        self.table = []
        for i in range(len(up)):
            self.table.append(up[i:]+up[:i])
            
    def generateTable(self):
        return self.table
    
    def padding(self, plain, key):
        panjangPlain = len(plain)
        keyPadding = key * panjangPlain
        return keyPadding[:panjangPlain]
            
    def encrypt(self, plain, key):
        padding = self.padding(plain,key)
        table = self.generateTable()
        panjang_plain = len(plain)
        plainToIndex = []
        keyToIndex = []
        for z in plain.upper():
            plainToIndex.append(table[0].find(z))
        # print(plainToIndex)
        for i in padding.upper():
            for x in table:
                if x[0] == i:
                    keyToIndex.append(up.find(i))
        # print(keyToIndex)
        cipherText = ""
        indexNumber = 0
        for i in keyToIndex:
            for p in range(i,i+1):
                cipherText += table[int(p)][plainToIndex[indexNumber]]
            indexNumber +=1
        return cipherText        
                    
            
            
    
x = Vigenere()
print("Hasil enkripsi : ",x.encrypt("udinmakannasi", "tes"))
