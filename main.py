import random

num = []

x = int(input("Enter the number of dice: "))
y = int(input("Enter the number of sides: "))


def roll_dice(number_of_dice, number_of_sides):
    print("rolling", x, "dice with", y, "sides each...")
    for i in range(number_of_dice):
        a = random.randint(number_of_dice, number_of_sides)
        print("rolled", a)
        num.append(a)
    print("The total is", sum(num))
    print("The highest number rolled was ", max(num))


roll_dice(x, y)
