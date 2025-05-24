print("Wwlcome to the tip calculater!")
bill = int(input("What was the total bill? "))
tip = int(input(f"How much tip would you like to give? {10} , {12}, or {15}?"))
people = int(input("How much people to split the bill? "))
pay = (bill * (tip/100) + bill) / people
print(f"Each person should pay : {pay}" )