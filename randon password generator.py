import random
characters="qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+1234567890QWERTYUIOPASDFGHJKLZXCVBNM<>?"

pass_length=int(input("enter length of required password:"))
pass_count=int(input("enter the number of password required:"))

for i in range (0,pass_count):
    password=""
    for j in range (0,pass_length):
        pass_char=random.choice(characters)
        password=password+pass_char
    print("The generated password is:",password)
