from encrypt import Enkripsivigenere
from decrypt import Decryptvigenere
from string import ascii_uppercase as up

class VigenereTable:
    def __init__(self) -> None:
        self.table = []
        for i in range(len(up)):
            self.table.append(up[i:] + up[:i])

    def generateTable(self):
        return self.table

# Buat objek untuk enkripsi, dekripsi, dan tabel
vigenere_table = VigenereTable()
vigenere_encrypt = Enkripsivigenere()
vigenere_decrypt = Decryptvigenere()

# Tampilkan tabel Vigenere
print("Tabel Vigenere:")
for row in vigenere_table.generateTable():
    print(" ".join(row))

# Input dari pengguna
plain_text = input("\nMasukkan plaintext: ")
key = input("Masukkan key: ")

# Enkripsi
cipher_text = vigenere_encrypt.encrypt(plain_text, key, vigenere_table.generateTable())
print("\nHasil enkripsi: ", cipher_text)

# Dekripsi
decrypted_text = vigenere_decrypt.decrypt(cipher_text, key, vigenere_table.generateTable())
print("Hasil dekripsi: ", decrypted_text)
