import random


print("----------------This is the Dice Game----------------")
start_game = input('Are you ready to start the game - "Yes" - "No": ')



def roll_dice():
	
	number_rolled= random.randint(1,6)

	
	return number_rolled



while start_game == "yes":
	
	print(roll_dice())
	start_game = input('Do you want to roll again? - "Yes" - "No": ')
	
	

print ("Thanks for playing!")



