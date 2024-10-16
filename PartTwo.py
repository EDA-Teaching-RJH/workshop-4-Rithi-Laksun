def main():
  drinksmenu = {'Coffee', 'Latte', 'Iced tea'}
  changeset = {'50p', '20p', '10p', '5p'}
  

  print("You can only pay with cash or 50p, 20p, 10p and 5p in this Coffee Machine")

  drinks = input("What drink would you like: Coffee, Latte or Iced tea: ")

  if drinks.casefold() == 'coffee':
    cost = 2.00
    shot = input("Do you want an extra shot for extra 50p? yes or no: ")
    if shot == "yes":
       cost = cost + 0.5
    else:
       pass
  elif drinks.casefold() == 'latte':
      cost = 2.50
  elif drinks.casefold() == 'iced tea':
      cost = 1.50
  else:
      print("Sorry we don't have it.")
      exit()

  cost = cost
  print("It's £", cost, "please pay by cash or coins")
  change = input("How much would you like to give: ")

  if change in changeset:
      change1 = float(change.replace("p", ""))
      give = cost - (change1 / 100)
      if change1 >= 0.75 and change1 < 0.75:
        print("Cost left to pay:", give)
      else:
        pass
  else:
      change = float(change)
      give = cost - change
      change >= 0.75
      print("Cost left to pay:", give)

  if give <= 0:
      g = abs(give)
      print("Here's your change: £", g)
  else:
      while give > 0:
        x = input("Sorry that wasn't enough. How much more would you like to give: ")
        if x in changeset:
          x1 = int(x.replace("p", ""))
          give = give - (x1 / 100)
          print("Cost left to pay:", give)
        elif x == int(x):
          x = int(x)
          give = give - x
        else:
          print("You have paid fully thank you!")
          break

  if cost == 0:
      print("You have paid fully thank you!")
  else:
      pass

main()
