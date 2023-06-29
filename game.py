print("Welcome to Landscaper!")

money = 0
has_tools = False

user_input = input("What is your name:")
print("Hello, " + user_input + "! You are starting a landscaping business, but you only have your teeth to start out with. You can make $1 a day cutting lawns this way.")

while True:
    action = input("What would you like to do? work/check funds/buy tool/quit: ")

    if action == "work":
      if has_tools:
        money += 5
        print("You used your scissors to cut lawns and earned $5!")
      else:
        money += 1
        print("You cut lawns and earned $1!")
    elif action == "check funds":
        print(f"You currently have ${money}.")
    elif action == "buy tool":
        if money >= 5:
            has_tools = True
            money -= 5
            print("You've purchased a pair of rusty scissors for $5!")
        else: 
            print("You don't have enough funds to buy scissors")
    elif action == "quit":
        break
    else:
        print("Invalid. Please try again.")