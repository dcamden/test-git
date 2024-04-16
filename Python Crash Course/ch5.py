# Starts on page 109
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# checking for inequality
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# requested_topping = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_topping #will come back true
# 'pepperoni' in requested_topping #will come back false

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish")

# Boolean expressions
# game_active = True
# can_edit = False

# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("Sorry, you are too young to vote")

# age = 3

# if age < 4:
#     print("Your admission cost is $0")
# elif age > 4  and age <= 17:
#     print("Your admission cost is $5")
# else:
#     print("Your admission cost is $10)")

# age = 3
# if age <4:
#     price = 0
# elif age <18:
#     price = 5
# else:
#     price = 10
# print("Your admission cost is $" + str(price) + ".")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")