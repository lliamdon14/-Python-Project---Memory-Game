import random
import os
import time
def clear_screen():
	os.system("cls")

def two():

	list1=[[0,0],[0,0]]

	counter = 0
	while counter<2:		#initialization of the 2x2 board
		isEmpty= True
		randomrow=random.randint(0,1)	#randomization of row 
		randomcolumn=random.randint(0,1) #randomization of column
		while isEmpty:
			if list1[randomrow][randomcolumn]==0: 	#the randomized numbers above were use as index where the random number will be put
				list1[randomrow][randomcolumn]=counter
				isEmpty=False
			else:
				randomrow=random.randint(0,1)	#if the first condition fails, it would iterate randomization
				randomcolumn=random.randint(0,1) #randomization of column
		counter= counter+1

	counter = 0				#the loop was performed twice to randomize the numbers in pair
	while counter<2:		
		isEmpty= True
		randomrow=random.randint(0,1)	
		randomcolumn=random.randint(0,1) 
		while isEmpty:
			if list1[randomrow][randomcolumn]==0: 	#
				list1[randomrow][randomcolumn]=counter
				isEmpty=False
			else:
				randomrow=random.randint(0,1)	
				randomcolumn=random.randint(0,1) 
		counter= counter+1
	
	return list1
def twoduplicate():
	list1duplicate={0:["*","*"],1:["*","*"]}
	return list1duplicate

def faketwoduplicate():	
	list1duplicate={0:["*","*"],1:["*","*"]}
	return list1duplicate
#--------------------------------------------------------------------------------

def four():

	list2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

	counter = 0
	while counter<9:		#initialization of the 4x4 board
		isEmpty= True
		randomrow=random.randint(0,3)	#randomization of row
		randomcolumn=random.randint(0,3) #randomization of column
		while isEmpty:
			if list2[randomrow][randomcolumn]==0: 	
				list2[randomrow][randomcolumn]=counter
				isEmpty=False
			else:
				randomrow=random.randint(0,3)	#randomization of row
				randomcolumn=random.randint(0,3) #randomization of column
		counter= counter+1

	counter = 0
	while counter<9:		
		isEmpty= True
		randomrow=random.randint(0,3)	#randomization of row
		randomcolumn=random.randint(0,3) #randomization of column
		while isEmpty:
			if list2[randomrow][randomcolumn]==0: 	
				list2[randomrow][randomcolumn]=counter
				isEmpty=False
			else:
				randomrow=random.randint(0,3)	#randomization of row
				randomcolumn=random.randint(0,3) #randomization of column
		counter= counter+1

	return list2

def fourduplicate(): 
	list2duplicate={0:["*","*","*","*"],1:["*","*","*","*"],2:["*","*","*","*"],3:["*","*","*","*"]}
	return list2duplicate

def fakefourduplicate():
	list2duplicate={0:["*","*","*","*"],1:["*","*","*","*"],2:["*","*","*","*"],3:["*","*","*","*"]}
	return list2duplicate


#---------------------------------------------------------------------
def eight():
	list3= [[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0]]

	counter = 0
	while counter<33:		#initialization of the 2x2 board
		isEmpty= True
		randomrow=random.randint(0,7)	#randomization of row
		randomcolumn=random.randint(0,7) #randomization of column
		while isEmpty:
			if list3[randomrow][randomcolumn]==0: 	#
				list3[randomrow][randomcolumn]=counter
				isEmpty=False
			else:
				randomrow=random.randint(0,7)	#randomization of row
				randomcolumn=random.randint(0,7) #randomization of column
		counter= counter+1

	counter = 0
	while counter<33:		#initialization of the 2x2 board
		isEmpty= True
		randomrow=random.randint(0,7)	#randomization of row
		randomcolumn=random.randint(0,7) #randomization of column
		while isEmpty:
			if list3[randomrow][randomcolumn]==0: 	#
				list3[randomrow][randomcolumn]=counter
				isEmpty=False
			else:
				randomrow=random.randint(0,7)	#randomization of row
				randomcolumn=random.randint(0,7) #randomization of column
		counter= counter+1

	return list3

def eightduplicate():
	list3duplicate= {0:["*","*","*","*","*","*","*","*"],
			1:["*","*","*","*","*","*","*","*"],
			2:["*","*","*","*","*","*","*","*"],
			3:["*","*","*","*","*","*","*","*"],
			4:["*","*","*","*","*","*","*","*"],
			5:["*","*","*","*","*","*","*","*"],
			6:["*","*","*","*","*","*","*","*"],
			7:["*","*","*","*","*","*","*","*"]}

	return list3duplicate

def fakeeightduplicate():
	list3duplicate= {0:["*","*","*","*","*","*","*","*"],
			1:["*","*","*","*","*","*","*","*"],
			2:["*","*","*","*","*","*","*","*"],
			3:["*","*","*","*","*","*","*","*"],
			4:["*","*","*","*","*","*","*","*"],
			5:["*","*","*","*","*","*","*","*"],
			6:["*","*","*","*","*","*","*","*"],
			7:["*","*","*","*","*","*","*","*"]}
	return list3duplicate

#-----------------------------------
#main code


twoduplicate = twoduplicate() 
faketwoduplicate= faketwoduplicate()
a= two()
b=four()
c= eight()
fourduplicate = fourduplicate()
fakefourduplicate= fakefourduplicate()
eightduplicate= eightduplicate()
fakeeightduplicate = fakeeightduplicate()
dict_two = {}
dict_four = {}
dict_eight = {}
while True:
	print("-----Menu-----")
	print("(1) 2x2 board")
	print("(2) 4x4 board")
	print("(3) 8x8 board")
	print("(4) Exit")
	choice = int(input("Choose Mode:"))
	score_count_two = 0
	score_count_four = 0
	score_count_eight = 0
	if choice==1:
		clear_screen()
		while True:
			print("2x2 Board")
			score_count_two = 0
			print("-----Menu-----")
			print("(1) Start Game")
			print("(2) High Scores")
			print("(3) Exit")
			
			menu_2 = int(input("Choose Mode:"))
			clear_screen()
			counter = 0
			if menu_2 == 1:
				while True:
					if counter == 0:
						for k,v in twoduplicate.items():
							print(k,v)
						list1duplicate2=[["*","*"],["*","*"]]
						print("Choose two card to open in coordinate (x,y):")
						print("---X is vertical(0-1), Y is horizontal (0-1)---")
						a1 = int(input("Input first coordinate x: "))
						b1 = int(input("Input first coordinate y: "))
						print("You chose: (",a1,",",b1,")")
						a2 = int(input("Input second x coordinate to open: "))
						b2 = int(input("Input second y coordinate to open: "))
						print("You chose: (",a2,",",b2,")")
						
						
						if (a1 == a2) & (b1 == b2):
							clear_screen()
							print("Invalid Input")
							continue

						if (a1 or a2) > 1:
							clear_screen()
							print("Input out of range!! Try again")
							continue

						if (b1 or b2) >1:
							clear_screen()
							print("Input out of range!! Try again")
							continue

						valuecoordinate1 = a[a1][b1]
						valuecoordinate2 = a[a2][b2]

				
						if a[a1][b1] == a[a2][b2]: #i use indexing to check if the value in the specific index is equal (to check if the pair is correct)
							clear_screen() #clears the screen if the answer is right
							twoduplicate[a1][b1]=valuecoordinate1
							twoduplicate[a2][b2]=valuecoordinate2
							x = twoduplicate.values()
							clear_screen()
							print("CORRECT!!")
							score_count_two = score_count_two + 1
							print("Number of Moves:" ,score_count_two)

							#----------checking if all the elements of the list were exhausted. If yes, the player won and the game is finished------
							list1=[]
							for i in x:
								for k in i:
									list1.append(k)
							for i in list1:
								if list1.count("*") >= 2:
									break
								else:
									print("Congratulations!! You won!!")
									print("Your score is", score_count_two)
									counter = counter+1
									save_score_two = input("Please enter your name: ")
									dict_two[save_score_two] = score_count_two
									import highscores_function
									highscores_function.save_two(dict_two) #saving the scores to an external
									
									print("Your score has been saved to scores!")
									break
							#-------------------------------------	
								
						else:	#this part will show the chosen pair if it isn't a right pair
							faketwoduplicate[a1][b1]=valuecoordinate1		
							faketwoduplicate[a2][b2]=valuecoordinate2
							for k,v in faketwoduplicate.items():
								print(k,v)
							print("TRY AGAIN!!!")
							faketwoduplicate[a1][b1]="*"	#this will hide the wrong pair of answer
							faketwoduplicate[a2][b2]="*"
							time.sleep(4)
							clear_screen()
							score_count_two = score_count_two + 1
							print("Number of Moves:" ,score_count_two)
							
							continue
					if counter != 0:
						break
			if menu_2 == 2: 
				import highscores_function
				print("Scores:")
				x = highscores_function.load_two()
				
				
			if menu_2 == 3:
				break
				
	if choice==2: 
		clear_screen()
		while True:
			print("4x4 Board")
			score_count_four = 0

			print("-----Menu-----")
			print("(1) Start Game")
			print("(2) High Scores")
			print("(3) Exit")

			menu_3 = int(input("Choose Mode:"))
			clear_screen()
			counter = 0
			if menu_3 == 1:
				while True:
					if counter ==0:
						for k,v in fourduplicate.items():
							print(k,v)
						list2duplicate2=[["*","*","*","*"],["*","*","*","*"],["*","*","*","*"],["*","*","*","*"]]
						print("Choose two card to open in coordinate (x,y):")
						print("---X is vertical(0-3), Y is horizontal (0-3)---")
						a1 = int(input("Input first coordinate x: "))
						b1 = int(input("Input first coordinate y: "))
						print("You chose: (",a1,",",b1,")")
						a2 = int(input("Input second x coordinate to open: "))
						b2 = int(input("Input second y coordinate to open: "))
						print("You chose: (",a2,",",b2,")")
						
						if (a1 == a2) & (b1 == b2):
							clear_screen()
							print("Invalid Input")
							continue
						if (a1 or a2) > 3:
							clear_screen()
							print("Input out of range!! Try again")
							continue

						if (b1 or b2) >3:
							clear_screen()
							print("Input out of range!! Try again")
							continue
						valuecoordinate1 = b[a1][b1]
						valuecoordinate2 = b[a2][b2]

						if b[a1][b1] == b[a2][b2]: #i use indexing to check if the value in the specific index is equal (to check if the pair is correct)
							clear_screen() #clears the screen if the answer is right
							print("CORRECT!!")
							fourduplicate[a1][b1]=valuecoordinate1
							fourduplicate[a2][b2]=valuecoordinate2
							y=fourduplicate.values()
							clear_screen()
							score_count_four = score_count_four + 1
							print("Number of Moves:" ,score_count_four)
						

						#----------checking if all the elements of the list were exhausted. If yes, the player won and the game is finished------
							list2=[]
							for i in y:
								for k in i:
									list2.append(k)
							for i in list2:
								if list2.count("*") >= 2:
									break
								else:
									print("Congratulations!! You won!!")
									print("Your score is", score_count_four)
									counter = counter+1
									save_score_four = input("Please enter your name:")
									dict_four[save_score_four] = score_count_four
									import highscores_function_four
									highscores_function_four.save_four(dict_four)
									print("Your score has been saved to scores!")
							
									break	


						else:
							fakefourduplicate[a1][b1]=valuecoordinate1		
							fakefourduplicate[a2][b2]=valuecoordinate2
							for k,v in fakefourduplicate.items():
								print(k,v)
							print("TRY AGAIN!!!")
							fakefourduplicate[a1][b1]="*"	#this will hide the wrong pair of answer
							fakefourduplicate[a2][b2]="*"
							time.sleep(4)
							clear_screen()
							score_count_four = score_count_four + 1
							print("Number of Moves:" ,score_count_four)
							
							continue
					if counter !=0:
						break

			if menu_3 == 2:
				import highscores_function
				print("Scores:")
				x = highscores_function.load_four()
			if menu_3 == 3:
				break


	if choice == 3:
		clear_screen()
		while True:
			print("8x8 Board")
			score_count_eight = 0

			print("-----Menu-----")
			print("(1) Start Game")
			print("(2) High Scores")
			print("(3) Exit")
			

			menu_4 = int(input("Choose Mode:"))
			clear_screen()
			counter = 0
			if menu_4 ==1:
				while True:
					if counter ==0:
						for k,v in eightduplicate.items():
							print(k,v)
						list3duplicate= {0:["*","*","*","*","*","*","*","*"],
						1:["*","*","*","*","*","*","*","*"],
						2:["*","*","*","*","*","*","*","*"],
						3:["*","*","*","*","*","*","*","*"],
						4:["*","*","*","*","*","*","*","*"],
						5:["*","*","*","*","*","*","*","*"],
						6:["*","*","*","*","*","*","*","*"],
						7:["*","*","*","*","*","*","*","*"]}
						print("Choose two card to open in coordinate (x,y):")
						print("---X is vertical(0-7), Y is horizontal (0-7)---")
						a1 = int(input("Input first coordinate x: "))
						b1 = int(input("Input first coordinate y: "))
						print("You chose: (",a1,",",b1,")")
						a2 = int(input("Input second x coordinate to open: "))
						b2 = int(input("Input second y coordinate to open: "))
						print("You chose: (",a2,",",b2,")")
					
						if (a1 == a2) & (b1 == b2):
							clear_screen()
							print("Invalid Input")
							continue
						if (a1 or a2) > 7:
							clear_screen()
							print("Input out of range!! Try again")
							continue

						if (b1 or b2) >7:
							clear_screen()
							print("Input out of range!! Try again")
							continue

						
						valuecoordinate1 = c[a1][b1]
						print("The value of coordinate 1 is", + valuecoordinate1)
						valuecoordinate2 = c[a2][b2]
						print("The value of coordinate 2 is", + valuecoordinate2)


						if c[a1][b1] == c[a2][b2]: #i use indexing to check if the value in the specific index is equal (to check if the pair is correct)
							
							clear_screen() #clears the screen if the answer is right
							print("CORRECT!!")
							eightduplicate[a1][b1]=valuecoordinate1
							eightduplicate[a2][b2]=valuecoordinate2
							z = fourduplicate.values()
							clear_screen
							score_count_eight = score_count_eight + 1
							print("Number of Moves:" ,score_count_eight)
						#----------------list checking--------

							list3=[]
							for i in z:
								for k in i:
									list3.append(k)
							for i in list3:
								if list3.count("*") >= 2:
									break
								else:
									print("Congratulations!! You won!!")
									print("Your score is", score_count_eight)
									counter = counter+1
									save_score_eight = input("Please enter your name: ")
									dict_eight[save_score_eight] = score_count_eight
									import highscores_function
									highscores_function.save_eight(dict_eight)
									print("Your score has been saved to scores!")
									break	

						else:
							fakeeightduplicate[a1][b1]=valuecoordinate1		
							fakeeightduplicate[a2][b2]=valuecoordinate2
							for k,v in fakeeightduplicate.items():
								print(k,v)
							print("TRY AGAIN!!!")
							fakeeightduplicate[a1][b1]="*"	#this will hide the wrong pair of answer
							fakeeightduplicate[a2][b2]="*"
							time.sleep(4)
							clear_screen()
							score_count_eight = score_count_eight + 1
							print("Number of Moves:" ,score_count_eight)
							
							continue
					if counter !=0:
						break

			if menu_4 ==2:
				import highscores_function
				print("Scores: ")
				x = highscores_function.load_eight()
			if menu_4 ==3:
				break


	if choice == 4:
		break