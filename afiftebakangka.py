#milih angka random int 1-100
import random
num = random.randint(1,100)
score = 100
#user menebak angka yang dipilih komputer
print("Coba tebak angka cuy")
while True:
    guess = int(input("Berapa nih? : "))
    if guess < num:
        print("Kurang dikit")
        score -=10
        
    elif guess > num:
        print("Kelewat cuy")
        score -=10
        
    else:
        print("Nah bener")
        break
    print("Your score is : ", score)
    if score == 0:
        print("Game Over")
        break