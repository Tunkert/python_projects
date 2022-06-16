# create mad lib

# take in user input for mad libs
body_part = input("Enter a body part: ")
verb = input("Enter an verb: ")
verb_2 = input("Enter a verb: ")
land_feature = input("Enter a land feature: ")
thing = input("Enter a thing: ")

# create madlib f string
madlib = f"Trying to find cheap eggs is a pain in the {body_part}. \
I have a bunch of stores selling egss but they {verb} {thing}. \
Sometimes I just want to {verb_2} off of the {land_feature}."

# print madlib back to the user
print(madlib)