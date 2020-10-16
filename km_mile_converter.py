
print("Hi user!\n\nI am a kilometer to mile converter.")
mile = 0.621371192
proceed = "Y"
proceed = proceed.lower()


while proceed == "y":
    print("Enter amount you'd like to convert into miles: ")
    km = int(input(""))
    print(str(km) + " kilometers equals to: " + str(km * 0.621371192) + "miles")
    proceed = input("Type Y if you wish to do another conversion: ")
    proceed = proceed.lower()

print("bye bye")
