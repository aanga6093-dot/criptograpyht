import string 
import random
import hashlib

ASCII = string.ascii_letters + string.digits + string.punctuation

def generate_hash_string(number, length=600):
    result = ""
    counter = 0

    while len(result) < length:
        data = f"{number}:{counter}".encode()

        digest = hashlib.sha256(data).digest()
        for byte in digest:
            result += ASCII[byte % len(ASCII)]
            if len(result) >= length:
                break

        counter += 1

    return result



class DvHelman:
    def __init__(self,public_key,private_key):
        self.private_key = private_key
        self.public_key = public_key
        
    def my_result(self):
        return pow(
            self.public_key["awal"],
            self.private_key,
            self.public_key["modulus"]
        )   
        
    def get_same_key(self,she_result):
        return pow(
            she_result,
            self.private_key,
            self.public_key["modulus"]
        )
        
            

class OneTipe:
    @staticmethod        
    def endript(plain_text,key):
        result = [
            chr((ord(x)+ord(y)) + 33)
            for x,y in zip(plain_text,key)
        ]
        return "".join(result)  
         
    @staticmethod 
    def decript(cipher_text, key):
        result = [
            chr((ord(x) - ord(y)) - 33)
            for x, y in zip(cipher_text, key)
        ]
        return "".join(result)  
        


print("""
⣿⣿⡿⢰⣿⣿⣹⣿⢇⡇⣼⠀⢺⣿⣿⡿⢸⣿⣿⣿⢠⢹⣿⣿⣿⡈⣿⣿
⣿⣿⣿⢧⣿⡿⢻⢱⡟⣼⡇⣿⠀⠘⣿⡾⡇⡼⣿⣿⣿⢸⣦⢫⢻⣿⣇⢹⣿
⣿⣿⡿⣼⡿⠙⣾⢸⢡⣿⣷⠻⣧⣀⣹⣷⣣⣧⠻⠿⣩⣠⣿⣧⣃⠻⣧⢸⣿
⣿⣿⡇⣬⣶⣶⣿⣷⣾⣭⣭⣿⣿⣿⣿⣿⣿⣿⣾⣭⣭⣷⣿⣿⣿⣷⣌⡆⣿
⣿⣿⡇⠋⣉⡉⠉⠉⠙⠻⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠉⢀⣈⡁⣻
⣿⡿⡇⣾⣿⡇⠀⠲⠢⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠐⠒⠄⠀⢀⣿⡇⣿
⣿⣷⢇⣿⣿⣿⡰⢶⠶⠖⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡠⠶⠶⠶⣸⣿⢇⢿
⣿⣿⡎⠸⣿⣿⡿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢟⠟⣨⣿
⣿⣿⡼⡴⣬⢑⣎⣿⣿⣿⣿⣿⣏⣛⣛⣛⣛⣛⣹⣿⣿⣿⣿⣯⣏⣬⣼⢸⡟
⢿⣿⡇⢱⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠻⠋⣾
⡎⣹⣧⠈⢿⢨⣤⣉⠶⠝⢟⣝⠿⢟⠻⡟⡻⣿⠟⣝⠟⡴⠮⢁⣫⣵⢲


WELCOME!
""")


def main():
    while True:
        print("<buat public key bersama:")
                        
        user1 = DvHelman(
            public_key={
                "awal": int(input("<first numbers:")),
                "modulus": int(input("<modulus numbers: "))
            },
            private_key=random.randint(1, 1000000)
        )
        
        my_result = user1.my_result()
        print("<kirim key this ke bro:", my_result)

        if input("lanjut y/n:") != "y":
            return

        user2_result = int(input("<masukan key dari kiriman bro:"))
        print("membuat kunci bersama...")
        
        key_bersama = user1.get_same_key(user2_result)

        print("key bersama berhasil di buat!\n")
        print("key:", key_bersama, "\n\n")
        print("<mulai komunikasi>")

        for i in range(5):
            print("PILIH OPSI!\n\n[1].kirim\n[2].terima\n[3].exit\n[4].new_key")
            pilihan = int(input(":"))

            if pilihan == 1:
                text = input("<input pesan:")
                print("meng endripsi... \n")
                syper_txt = OneTipe.endript(
                    text,
                    generate_hash_string(key_bersama,length=len(text))
                    )
                print(f"hasil: {syper_txt}")
            elif pilihan == 2:
                syper_text = input("<input syper text:")
                plain_txt = OneTipe.decript(
                    syper_text,
                    generate_hash_string(key_bersama,length=len(syper_text))
                )
                print("meng endripsi... \n")
                print("hasil: ", plain_txt)
            elif pilihan == 3:
                return
            elif pilihan == 4:
                break    

        
if __name__ == "__main__":
    main()

    
