print("Welcome to Landscaper!")

money = 0
user_tools = "teeth"

user_input = input("What is your name:")
print("Hello, " + user_input + "! You are starting a landscaping business, but you only have your teeth to start out with. You can make $1 a day cutting lawns this way.")

while True:
    action = input("What would you like to do? work/check funds/quit: ")

    if action == "work":
        money += 1
        print("You cut lawns and earned $1!")
    elif action == "check funds":
        print(f"You currently have ${money}.")
    elif action == "quit":
        break
    else:
        print("Invalid. Please try again.")
