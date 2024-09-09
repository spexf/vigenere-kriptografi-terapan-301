from string import ascii_uppercase as up

class Decryptvigenere:
    def padding(self, text, key):
        panjang_text = len(text)
        keyPadding = key * panjang_text
        return keyPadding[:panjang_text]

    def decrypt(self, cipher, key, table):
        padding = self.padding(cipher, key)
        cipherToIndex = [up.find(z) for z in cipher.upper()]
        keyToIndex = [up.find(i) for i in padding.upper()]

        plainText = ""
        for i, c_index in enumerate(cipherToIndex):
            row = table[keyToIndex[i]]
            plainText += up[row.find(up[c_index])]

        return plainText
