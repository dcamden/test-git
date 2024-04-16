# Infinite Loop
# x = 0

# while True:
#     print(x)
#     x += 1
    
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Tell me your name!   ")
# print("Hello " + name+ "!")

# prompt = "If you tell us who you are, we can personalise the messages you see."
# prompt += "\nWhat is yout first name?   "

# name = input(prompt)
# print("\nHello " + name + "!")

### Input stores variable as string, not integer. If you store a number in input, you cannot use it as an integer example:
# age = input("How old are you")
# print(age)
# age +=1

# height = input("How tall are you, in inches?   ")
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older")

# number = input("Give me a number, and I will tell you if it's even or odd")
# number = int(number)

# if number % 2 ==0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

# number = 1
# while number <= 5:
#     print(number)
#     number +=1

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program.   "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

#Flag

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program.   "

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# number = 0
# while number <=10:
#     number += 1
#     if number % 2 ==0:
#         continue
#     print(number)

#Start with the users that need to be verified, and an empty list to hold confirmed users

# unconfirmed_users = ['Alice', 'brian', 'candace']
# confirmed_users = []

#Verify each user unitl there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)

# #Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb today?" )
#     responses[name] = response
#     repeat = input("Would you like to let another person respond?  (yes/no) ")
#     if repeat == 'no':
#         polling_active = False

# print("\n--- Polling Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")
