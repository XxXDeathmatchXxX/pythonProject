number_of_tickets = int(input("Enter amount of tickets: "))

tickets = 0

for i in range(number_of_tickets):
    age = int(input(f"Enter age of {i + 1} customer: "))
    if age < 18:
        print('For young customer ticket is free ')
        continue
    elif 18 <= age <= 25:
        print('for this customer amount will be : 990')
        tickets += 990
    else:
        print('For this customer amount will be: 1390')
        tickets += 1390

if number_of_tickets > 3:
    print("Sum to pay with sale 10% is : ", tickets - tickets / 100 * 10)
else:
    print("Total sum is :", float(tickets))


