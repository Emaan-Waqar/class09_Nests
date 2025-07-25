print("Ride options: ")
print("1. Bike")  
print("2. Car")

choice = int(input("Enter your preference: "))

if choice == 1:
    print("What type of bike: ")
    print("1. Motorbike")
    print("2. Scooter")
    choice2= int(input("Enter type of bike: "))    
    if choice2 == 1:
        print("You have selected Motorbike")
    else:
        print("You have selected a scooter")
elif choice == 2:
    print("What type of car: ")
    print("1. sedan")
    print("2. hatchback")
    print("3. SUV")
    choice3 = int(input("Enter the type of car: "))
    if choice3 ==1:
        print("You have selected sedan")
    elif choice3 ==2:
        print("You have selected hatchback")
    else: 
        print("You have selected SUV")    
else:
    print("ًWrong choice")        