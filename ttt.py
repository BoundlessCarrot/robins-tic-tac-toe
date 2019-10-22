import random

row1= [0, 0, 0]
row2= [0, 0, 0]
row3= [0, 0, 0]

map = [row1, row2, row3]

game_over = 'false'
firstPlayer = random.randint(0, 2)
player1Move = "a0"
player2Move ="a0"
xglobal = 0
yglobal = 0
index = {"a":0, "b":1, "c":2}
		
def print_board():
	for i in range(0, 3, 1):                       
		print("|", end= ' ', flush='true')
		for x in range(0, 3, 1):
			if map[i][x] == 0:
				print(" ", end= ' ', flush='true')
			elif map[i][x] == 1:
				print("O", end= ' ', flush='true')
			elif map[i][x] == 4:
				print("X", end= ' ', flush='true')
		print("|")

def print_board_val():
	for i in range(0, 3, 1):
		for x in range(0, 3, 1):
			print(map[i][x], end= ' ', flush='true')
		print("\n")
		
def inputFunc(x, y, i):
	print_board()
	winCheck()
		
	if i == 1:	
		print("Player 1's Turn")
		player1Move = input("Please input move:")
		#print(player1Move[0])
		x=index[player1Move[0]]
		y=int(player1Move[1])
		while map[x][y] != 0:
			player1Move = input("That slot is taken. Please input a new move:")
			x=index[player1Move[0]]
			y=int(player1Move[1])
		map[x][y] = 1
	elif i ==2:
		print("Player 2's Turn")
		player2Move = input("Please input move:")
		#print(player2Move[0])
		x=index[player2Move[0]]
		y=int(player2Move[1])
		while map[x][y] != 0:
			player1Move = input("That slot is taken. Please input a new move:")
			x=index[player1Move[0]]
			y=int(player1Move[1])
		map[x][y] = 4		
	
def playRound():
	x=0
	y=0
	if(firstPlayer == 0):
		#print(player1Move[0])
		x=index[player1Move[0]]
		y=int(player1Move[1])
		inputFunc(x, y, 1)
		#print(player2Move[0])
		x=index[player2Move[0]]
		y=int(player2Move[1])
		inputFunc(x, y, 2)		
	elif(firstPlayer == 1):
		#print(player2Move[0])
		x=index[player2Move[0]]
		y=int(player2Move[1])
		inputFunc(x, y, 2)
		#print(player1Move[0])
		x=index[player1Move[0]]
		y=int(player1Move[1])
		inputFunc(x, y, 1)
			
def winCheck():
	wincheck = 0
	for x in range(0, 3, 1):
		wincheck = 0
		for y in range(0, 3, 1):
					wincheck += map[x][y]
		if wincheck == 3:
			print("Player 1 Wins")
			game_over = 'true'
			exit()
		elif wincheck == 12:
			print("Player 2 Wins")
			game_over = 'true'
			exit() 	
	
	for y in range(0, 3, 1):
		wincheck = 0	
		for x in range(0, 3, 1):
			wincheck += map[x][y]
			if wincheck == 3:
				print("Player 1 Wins")
				game_over = 'true'
				exit() 
			elif wincheck == 12:
				print("Player 2 Wins")
				game_over = 'true'
				exit() 
	
		if map[0][0]+map[1][1]+map[2][2] == 3:
			print("Player 1 Wins")
			game_over = 'true'
			exit() 
		elif map[0][0]+map[1][1]+map[2][2] == 12:
			print("Player 2 Wins")
			game_over = 'true'
			exit() 
		elif map[0][2]+map[1][1]+map[2][0] == 3:
			print("Player 1 Wins")
			game_over = 'true'
			exit() 
		elif map[0][2]+map[1][1]+map[2][0] == 12:
			print("Player 2 Wins")
			game_over = 'true'
			exit() 
			
while(game_over == 'false'):
	playRound()
	#print_board_val()
	#game_over = 'true'