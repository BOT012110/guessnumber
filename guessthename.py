import random

def guess_the_number(x):
    randam = random.randint(1, x)
    guess = 0
    
    while guess != randam:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        
        if guess < randam:
            print("Sorry, number is too low")
        elif guess > randam:
            print("Sorry, number is too high")
    
    print(f"{randam} is Correct, Congratulation!!!")

def computer_guess(x):
    low = 1 
    high = x
    feedback = ""
    
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low  # or high doesn't matter
    
        feedback = input(f"if {guess} too high (H), is too low (L), is correct (C)??\n").lower()
         
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yea {guess} is correct!!!")
            

#guess_the_number(100)
computer_guess(100)