age = int(input("Enter age: "))

if age < 18:
    print("Not Eligible to Rent")
elif age <= 25:
    print("Extra Charges Apply")
else:
    print("No Extra Charges")
