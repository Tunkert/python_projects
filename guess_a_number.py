# create a program where user has to guess a random number

# import random so you can get a random integer
import random

# pick random number between 1 and 100
random_number = random.randint(1, 101)

# create user_guess variable and set to 0
user_guess = 0

# create function to see if user wants to keep playing
def still_play():
	# take input to see if they want to continue
		keep_playing = input("Do you want to keep playing. Enter 'n' to stop or anything else to continue: ")

		# check to see if they should keep playing
		if keep_playing == 'n':
			print("You lost. ")
			# break out of loop
			return 0

# loop while user_guess != random_number
while user_guess != random_number:
	# Have user enter a random number - check
	while True:
		try:
			user_guess = int(input("Enter a random integer between 1 and 100: "))
		except:
			# let user they didn't enter an integer
			print("Enter an integer, pal. Try again.")
		else:
			if user_guess >= 1 and user_guess <= 100:
				break
			else:
				# let user know the integer they entered wasn't between 1 and 100
				print("Listen buddy, you entered an integer that wasn't between 1 and 100. Try again.")

	# check user guess and give feedback
	if user_guess == random_number:
		print("You guessed right! You win!")
	elif user_guess < random_number:
		print("Your guess is too low.")
		if still_play() == 0:
			break
	else:
		print("Your guess is too high.")
		if still_play() == 0:
			break
