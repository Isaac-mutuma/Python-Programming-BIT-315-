#python code to check eligility of bonus for employees

salary = float(input("Enter your salary: "))
year_of_service = int(input("Enter your year of service: "))

if year_of_service > 5:
    bonus = salary * 0.05
    net_bonus = salary + bonus
    print("Your net bonus amount is: $" + str(net_bonus))
else:
    print("You are not eligible for a bonus.")