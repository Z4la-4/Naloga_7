
user_number = int(input("enter your number between 1 and 100: "))

for x in range(1,user_number+1):
    if (x % 3) == 0 and (x % 5) == 0:
        print("fizzbuzz")
    elif (x % 3) == 0:
        print("fizz")
    elif (x % 5) == 0:
        print("buzz")
    else:
        print(x)

