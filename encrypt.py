from string import ascii_uppercase as up

class Enkripsivigenere:
    def padding(self, plain, key):
        panjangPlain = len(plain)
        keyPadding = key * panjangPlain
        return keyPadding[:panjangPlain]

    def encrypt(self, plain, key, table):
        padding = self.padding(plain, key)
        plainToIndex = [table[0].find(z) for z in plain.upper()]
        keyToIndex = [up.find(i) for i in padding.upper()]

        cipherText = ""
        indexNumber = 0
        for i in keyToIndex:
            for p in range(i, i + 1):
                cipherText += table[int(p)][plainToIndex[indexNumber]]
            indexNumber += 1
        return cipherText
