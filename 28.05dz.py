#3
import random
class PasswordGenerator:
    def __init__(self , length , characters):
        self.length = length
        self.characters = characters
    def generate_password(self):
        password = ''
        for i in range(self.length):
            password += random.choice(self.characters)
        return password
rezult = PasswordGenerator(10 , 'DFH42!#%xfgn97876')
for i in range(3):
    print(f"Пароль: {rezult.generate_password()}")