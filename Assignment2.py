
#REFERENCE LIST
#John Aycock 2016-02-06 UNIVERSE MAP  [Computer program] available at http://pages.cpsc.ucalgary.ca/~aycock/231/as2-major.html
#John Aycock 2016-02-06 PLACING OBJECTS  [Computer program] available at http://pages.cpsc.ucalgary.ca/~aycock/231/as2-major.html
#John Aycock 2016-02-06 MOVEMENT COMMANDS [Computer program] available at http://pages.cpsc.ucalgary.ca/~aycock/231/as2-major.html
#John Aycock 2016-02-06  DOCK COMMAND [Computer program] available at http://pages.cpsc.ucalgary.ca/~aycock/231/as2-major.html
#The Dems 2012-10-31 EUCLIDEAN FORMULA [Calculation] available at http://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy

#imports random for attacking, imports time for destruct command
import random
import time

# variables that are assigned specifically for what they are
empty = '.'
enterprise = 'E'
klingon = 'K'
star = '*'
starbase = '#'
enterenergy = 250
klingons = 3

# creates the grid, which the game is played on 
map = [[empty for x in range(10)] for y in range(10)]

#places the enterprise randomly on the grid
for i in range(1):
	while True:	
		x_coor_enterprise = random.randrange(0, 10)
		y_coor_enterprise = random.randrange(0, 10)
		if map[x_coor_enterprise][y_coor_enterprise] =='.':
			break
	map[x_coor_enterprise][y_coor_enterprise] = enterprise

#places all klingons on the map randomly
for i in range (1):
	while True:
		x_coor_klingon1 = random.randrange(0, 10)
		y_coor_klingon1 = random.randrange(0, 10)
		if map[x_coor_klingon1][y_coor_klingon1] =='.':
			break
	map[x_coor_klingon1][y_coor_klingon1] = klingon

for i in range (1):
	while True:
		x_coor_klingon2 = random.randrange(0, 10)
		y_coor_klingon2 = random.randrange(0, 10)
		if map[x_coor_klingon2][y_coor_klingon2] =='.':
			break
	map[x_coor_klingon2][y_coor_klingon2] = klingon

for i in range (1):
	while True:
		x_coor_klingon3 = random.randrange(0, 10)
		y_coor_klingon3 = random.randrange(0, 10)
		if map[x_coor_klingon3][y_coor_klingon3] =='.':
			break
	map[x_coor_klingon3][y_coor_klingon3] = klingon

#places 10 stars on the grid, randomly
for i in range (10):
	while True:
		x_coor_star = random.randrange(0, 10)
		y_coor_star = random.randrange(0, 10)
		if map[x_coor_star][y_coor_star] =='.':
			break
	map[x_coor_star][y_coor_star] = star

#starbase randomly placed some where on the grid
for i in range (1):
	while True:
		x_coor_starbase = random.randrange(0, 10)
		y_coor_starbase = random.randrange(0, 10)
		if map[x_coor_starbase][y_coor_starbase] =='.':
			break
	map[x_coor_starbase][y_coor_starbase] = starbase

print(map)

# finds the euclidean distance 
def klingon_distance():
	global klingon1
	global klingon2
	global klingon3
	from math import sqrt
	a = (int(x_coor_enterprise),int(y_coor_enterprise))
	b = (int(x_coor_klingon1),int(y_coor_klingon1))
# euclidean formula
	klingon1 = (sqrt(sum((a - b)**2 for a, b in zip(a, b))))
	klingon1 = (int(float(klingon1)))
	print("the distance between the Enterprise and Klingon1 is:", klingon1)

	a = (int(x_coor_enterprise),int(y_coor_enterprise))
	b = (int(x_coor_klingon2),int(y_coor_klingon2))
	klingon2 = (sqrt(sum((a - b)**2 for a, b in zip(a, b))))
	klingon2 = (int(float(klingon2)))
	print("the distance between the Enterprise and Klingon2 is:", klingon2)

	a = (int(x_coor_enterprise),int(y_coor_enterprise))
	b = (int(x_coor_klingon3),int(y_coor_klingon3))
	klingon3 = (sqrt(sum((a - b)**2 for a, b in zip(a, b))))
	klingon3 = (int(float(klingon3)))
	print("the distance between the Enterprise and Klingon3 is:", klingon3)

# this part of the code tells you if the klingon is close enough to hit the enterprise
# and the probability for  if it will hit or not

def klingon_hit():
	global enterenergy
	if klingon1 <= 3:
		if map[x_coor_klingon1][y_coor_klingon1] == "K":
			chancehit1 = random.randrange(0,101)
			if chancehit1 <= 42:
				if klingon1 == 1:
					enterenergy = enterenergy - 50
				if klingon1 == 2:
					enterenergy = enterenergy - 25
				if klingon1 == 3:
					enterenergy = enterenergy - 16.7
				print("klingon1 has hit you, you have:", float(enterenergy), " energy left")
			else:
				print("Klingon 1 missed, your turn.")	
		else:
			print("")

	if klingon2 <= 3:
		if map[x_coor_klingon2][y_coor_klingon2] == "K":
			chancehit2 = random.randrange(0,101)
			if chancehit2 <= 42:
				if klingon2 == 1:
					enterenergy = enterenergy - 50
				if klingon2 == 2:
					enterenergy = enterenergy - 25
				if klingon2 == 3:
					enterenergy = enterenergy - 16.7
				print("klingon2 has hit you, you have:", float(enterenergy), "energy left")
			else:
				print("Klingon 2 missed, your turn")	
		else: 
			print("")

	if klingon3 <= 3:
		if map[x_coor_klingon3][y_coor_klingon3] == "K":
			chancehit3 = random.randrange(0,101)
			if chancehit3 <= 42:
				if klingon3 == 1:
					enterenergy = enterenergy - 50
				if klingon3 == 2:
					enterenergy = enterenergy - 25
				if klingon3 == 3:
					enterenergy = enterenergy - 16.7
				print("klingon3 has hit you, you have:", float(enterenergy), "energy left")
			else:
				print("Klingon 3 missed, your turn")	
		else:
			print("")	
print("The Enterprises energy is:", enterenergy)

# this is the function which lets you dock and heal your enterprise for 250
def enterprise_heal():
	global enterenergy
	nearbase = False
	for y in range(int(y_coor_enterprise-1), int(y_coor_enterprise+2)):
		for x in range(int(x_coor_enterprise-1), int(x_coor_enterprise+2)):
			if x > 9 or y > 9 or x < 0 or y < 0:
				continue
			if map[x][y] == "#":
				nearbase = True
	if not nearbase:
		print (" You are not close enough to the starbase to dock")
	else:
		print ("your energy has been replenlished")
		enterenergy = 250
		print (enterenergy)



# this is the function that moves the enterprise, and where you want it to go
def enterprise_moving(move):
	global y_coor_enterprise
	global x_coor_enterprise
	# north direction
	if move == "north":
		map[x_coor_enterprise][y_coor_enterprise] = "."
		for i in range(1):
			while True:
				y_coordinate_north = (int(float(input("How far north would you like to move?"))))
				x_coor_enterprise = x_coor_enterprise - y_coordinate_north
				if x_coor_enterprise > 9 or x_coor_enterprise < 0:
					x_coor_enterprise = x_coor_enterprise + y_coordinate_north
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that is not a valid move, please enter a valid move within the board")
					(enterprise_moving(input("Which way would you like to move?")))
				if map[x_coor_enterprise][y_coor_enterprise] != ".":
					x_coor_enterprise = x_coor_enterprise + y_coordinate_north
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that space is taken, please choose another location")
					(enterprise_moving(input("Which way would you like to move?")))
				if x_coor_enterprise <= 9 and x_coor_enterprise >= 0:
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					return
	# south direction
	elif move == "south":
		map[x_coor_enterprise][y_coor_enterprise] = "."
		for i in range(1):
			while True:
				y_coordinate_south = (int(float(input("How far south would you like to move?"))))
				x_coor_enterprise = x_coor_enterprise + y_coordinate_south
				if x_coor_enterprise > 9 or x_coor_enterprise < 0:
					x_coor_enterprise = x_coor_enterprise - y_coordinate_south
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that is not a valid move, within the board")
					(enterprise_moving(input("Which way would you like to move?")))
				if map[x_coor_enterprise][y_coor_enterprise] != ".":
					x_coor_enterprise = x_coor_enterprise - y_coordinate_south
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that space is taken, please choose another location")
					(enterprise_moving(input("Which way would you like to move?")))
				if x_coor_enterprise <= 9 and x_coor_enterprise >= 0:
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					return
	# east direction
	elif move == "east":
		map[x_coor_enterprise][y_coor_enterprise] = "."
		for i in range(1):
			while True:
				x_coordinate_east = (int(float(input("How far east would you like to move?"))))
				y_coor_enterprise = y_coor_enterprise + x_coordinate_east
				if y_coor_enterprise > 9 or y_coor_enterprise < 0:
					y_coor_enterprise = y_coor_enterprise - x_coordinate_east
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that is not a valid move, within the board")
					(enterprise_moving(input("Which way would you like to move?")))
				if map[x_coor_enterprise][y_coor_enterprise] != ".":
					y_coor_enterprise = y_coor_enterprise - x_coordinate_east
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that space is taken, please choose another location")
					(enterprise_moving(input("Which way would you like to move?")))
				if y_coor_enterprise <= 9 and y_coor_enterprise >= 0:
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					return
	# west direction
	elif move == "west":
		map[x_coor_enterprise][y_coor_enterprise] = "."
		for i in range(1):
			while True:
				x_coordinate_west = (int(float(input("How far west would you like to move?"))))
				y_coor_enterprise = y_coor_enterprise - x_coordinate_west
				if x_coor_enterprise > 9 or x_coor_enterprise < 0:
					y_coor_enterprise = y_coor_enterprise + x_coordinate_west
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that is not a valid move, within the board")
					enterprise_moving(input("Which way would you like to move?"))
				if map[x_coor_enterprise][y_coor_enterprise] != ".":
					y_coor_enterprise = y_coor_enterprise + x_coordinate_west
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					print("Sorry that space is taken, please choose another location")
					(enterprise_moving(input("Which way would you like to move?")))
				if y_coor_enterprise <= 9 and y_coor_enterprise >= 0:
					map[x_coor_enterprise][y_coor_enterprise] = "E"
					return
	# else statement for if the entered command is not a valid direction
	else:
		print("Not a valid move")
		enterprise_moving(input("which way would you like to move?"))

# this function is based on if the enterprise will attack, and the probability it will attack, and
#measure how close it is ratio to hitting chance 
def enterprise_hitting(klingon_number):

	global enterenergy
	global klingons
	# takes away 50 energy for attacking
	enterenergy = enterenergy - 50
	# if statement for when the user inputs 1,2 or 3
	if klingon_number == "1":
		for i in range (1):	
			chance_to_hit = 75 // klingon1
			# random number generated between 0 and 100
			enter_chance = random.randrange(0, 100)
			# checking if the random number is less than, giving the range to hit
			if enter_chance <= chance_to_hit:
				#replaces the klingon with a "."
				map[x_coor_klingon1][y_coor_klingon1] = "."
				print("You have destroyed a klingon")	
				klingons = klingons - 1
			if enter_chance > chance_to_hit:
				# if the number generated is bigger than the chance than the print statement is run
				print("You missed")
	elif klingon_number == "2": 	
		for i in range(1):
			chance_to_hit = 75 // klingon2
			enter_chance = random.randrange(0, 100)
			if enter_chance <= chance_to_hit:
				map[x_coor_klingon2][y_coor_klingon2] = "."
				print("You have destroyed a klingon")	
				klingons = klingons - 1
			if enter_chance > chance_to_hit:
				print("You missed")
	elif klingon_number == "3":
		for i in range(1):
			chance_to_hit = 75 // klingon3
			enter_chance = random.randrange(0, 100)
			if enter_chance <= chance_to_hit:
				map[x_coor_klingon3][y_coor_klingon3] = "."
				print("You have destroyed a klingon")
				klingons = klingons - 1
			if enter_chance > chance_to_hit:
				print("You missed")
	# prints the current enterprise energy and the remaining amount of klingons
	print("The Enterprises energy is:", enterenergy)
	print ("there are", klingons, "klingons remaining")
# function that connects all functions and lets the program run smoothly
def all_functions(command):
	if command == "move":
		enterprise_moving(input("Which way would you like to move?"))
	elif command == "attack":
		enterprise_hitting(input("Which klingon would you like to attack 1, 2 or 3? "))
	elif command == "dock":
		enterprise_heal()
	elif command == "self destruct":
		n = 6
		for i in range(6):
			time.sleep((1))
			n = n - 1
			print(n)
		print("The Enterprise has 0 energy, Game Over, You Lose")
		quit()
	elif command == "quit":
		quit()
	else:
		print("Not a valid option")

#main, which runs everything

def main():
	
	all_functions(input("What would you like to do move, attack, dock, self destruct or quit?"))
	
	
#looping everything till the game is officially over
while klingons > 0 and enterenergy > 0:
	klingon_distance()
	if klingons <= 0:
		print("you have won")
	if enterenergy <= 0:
		print("you have run out of energy, you lose")
	klingon_hit()
	if klingons <= 0:
		print("you have won")
	if enterenergy <= 0:
		print("you have run out of energy, you lose")
	print("Your current location is:", "x=", y_coor_enterprise, "y=", x_coor_enterprise)
	main()
	if klingons <= 0:
		print("you have won")
	if enterenergy <= 0:
		print("you have run out of energy, you lose")
	print(map)

