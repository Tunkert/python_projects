# Get target value from user and check for errors
while True:
	try:
		# try to get high value as an integer
		high_value = int(input("What is the highest positive integer you want to check up to? "))
	except:
		# tell them that you should enter an integen
		print("Listen buddy, I said enter a positive integer.")
	else:
		if high_value > 0:
			break
		else:
			print("Listen buddy, I said enter a positive integer.")
	finally:
		pass

# create empty array to hold primes
primes_arr = []

# create boolean for checking for prime and initialize it to True
is_prime = True

# create a for loop to find primes
for number in range(2, high_value + 1):
	for other_number in range(2, number):
		if number % other_number == 0 and number != other_number:
			# if this happens set boolean to false, number is NOT prime
			is_prime = False
			# break out of loop
			break
		else:
			is_prime = True
	# check if is_prime is True and if so append number to primes_arr
	if is_prime == True:
		primes_arr.append(number)

# loop through numbers in primes array and print them
for value in primes_arr:
	if value != primes_arr[-1]:
		print(value, end=", ")
	else:
		print(value)

