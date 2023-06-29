print("Welcome to Landscaper!")

money = 0
tools = "teeth"

user_input = input("What is your name:")
print("Hello, " + user_input + "! You are starting a landscaping business, but you only have your teeth to start out with. You can make $1 a day cutting lawns this way.")

action = input("What would you like to do? work/check funds:")

if action == "work":
    money += 1
    print("You cut lawns using your teeth and made $1!")
elif action == "check funds":
    print(f'You currently have ${money}.')