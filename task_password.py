import random

def generate_password():
    capital_letters = ['A' , 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_letters = ['a' , 'b', 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    all = capital_letters + lower_letters + numbers
    password = []
    for i in range(1,random.randint(10,16)):
        character_random = random.choice(all)
        password.append(character_random)
    
    password = "".join(password)
    return password

def run():
    password = generate_password()
    print ("You new password is: " + password)
    
if __name__ == '__main__':
     run() 

