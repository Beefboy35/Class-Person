from random import randint


def is_value(a):
    if a.isdigit():

        if int(x) <= int(a) <= int(y):

            return True

        else:
            print(f"Maybe you should enter an integer FROM {x} TO {y}")
            return False
    else:
        print(f"Maybe you should enter an INTEGER from {x} to {y}")
        return False


print("Welcome to the number guessing game,buddy!")

x = input("What number should we start with? Enter the number:", )

print("Great!")
print("............")

y = input("And what number should we end with? Enter the number:", )
print("Awesome!")
print("............")
print("Perfect, let's start!")

number = randint(int(x), int(y))
cnt = 0

while True:
    num = input(f"Enter your value from {x} to {y}: ", )
    if is_value(num):
        num = int(num)
        if num == number:

            print("Congratulations! You guessed the correct number!")
            print("Your number of attempts is:", cnt)
            break
        elif num > number:
            cnt += 1
            print("Good choice, but...")
            print("Your number is greater than the right one! Try it again!")

        else:

            cnt += 1
            print("Good choice, but...")
            print("Your number is less than the right one! Try it again!")

print("Thank you for playing the game!")