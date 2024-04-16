# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()

# def greet_user(username):
#     """Display a simple greeting."""
#     print("Hello " + username.title() + "!")

# greet_user('Devin')

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='willie', animal_type='dog')

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(pet_name='willie')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet('willie')

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neartly formatted."""
#     full_name = first_name + " " + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + last_name
#     else:
#         full_name = first_name + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# # Start with some designs that need to be printed.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # Simulate creating a 3D print from the design.
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

# # Display all completed models
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# # Copy a list through a function without altering function
# function_name(list_name[:])

# Pass unknown number of arguments through a function

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

# import ch8module

# ch8module.make_pizza(16, 'pepperoni')
# ch8module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from module_name import function_name

# from ch8module import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from module_name import function_name as fn
# import ch8module as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Tell python to import every function in a module using *
# from ch8module import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')