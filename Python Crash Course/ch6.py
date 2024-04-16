# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print('You just earened ' + str(new_points) + ' points!')

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# can add or modify

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# alien_0['color'] = 'yellow'

# print(alien_0)

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original X-position: " + str(alien_0['x_position']))

# move the alien to the right
# Determine how far to move the alien based on its current speed

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alient.
#     x_increment = 3

# # The new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New x-position: " + str(alien_0['x_position']))

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("Sarah's favorite language is " +
#       favorite_languages['sarah'].title() +
#        ".")

#Looping 

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")

# for name in favorite_languages.keys():
#     print(name.title())

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in set(sorted(favorite_languages.values())):
#     print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

#make 30 aliens
# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# #Show how many aliens have been created
# print("Total number of aliens: " + str(len(aliens)))

# store list in dictionary

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)

