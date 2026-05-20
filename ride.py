print("Select your ride:\n1.Bike\n2.Car")

choice = int(input("Enter you choice : "))

if choice == 1:
    print("What type of bike? ")
    print("1.Scooter\n2.Motorcycle")

    choice2=int(input("Enter your choice2 : "))
    if choice2==1:
        print("You have selected scooty.")
    else:
        print("You have selected motorcylcle.")

elif(choice== 2):
    print("What type of Car?")
    print("1.Lambhorgini\n2.Tesla")
    choice3=int(input("Enter your choice3 : "))

    if choice3==1:
        print("You have selected Lambhorgini.")

    else:
     print("You have selected Tesla")

else:
    print("Wrong choice!")
