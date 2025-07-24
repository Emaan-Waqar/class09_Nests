medics= input("Do you have any medical condition (Y/N): ")
attendence= int(input("Enter your attendence: "))

if medics == "Y":
    print("You are eligible for exams")
else:
    print("You are not eligible")
    if attendence >=75:
        print("Eligible")    
    else:
        print("Not eligible")
