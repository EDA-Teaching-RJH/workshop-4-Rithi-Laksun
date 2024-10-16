drinks= ['Coffee', 'Latte', 'Iced tea']

drinks = input("What drink would you like: Coffee, Latte or Iced tea: ")

if drinks == 'Coffee':
    cost = 2.00
elif drinks == 'Latte':
    cost = 2.50
elif drinks == 'Iced tea':
    cost = 1.50
else:
    print("Sorry we don't have it. Please choose one of the 3 said")

print("It's £", cost, "please pay by cash or coins")
change = int(input("How much would you like to give: £"))

give = cost - change 

if give <= 0:
     g = abs(give)
     print("Here's your change: £", g)
#else:
    #for give in 