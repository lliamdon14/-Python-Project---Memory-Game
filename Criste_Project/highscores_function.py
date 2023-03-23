def save_two(dict_two):
	fp = open("Desktop/highscores_function.txt","a")
	for x,y in dict_two.items():
		data = x + ", " + str(y) + "\n"
		fp.write(data)
	fp.close()

def load_two(): #For loading the highscores
	dict2 = {}
	list1 = []
	fp2 = open("Desktop/highscores_function.txt","r")
	for line in fp2:
		list2 = line.split(",")
		print(list2[0],":", list2[1])
		dict2[list2[0]] = list1
	fp2.close()
	return dict2





def save_four(dict_four):
	fp = open("Desktop/highscores_function_four.txt","a")
	for x,y in dict_four.items():
		data = x + ", " + str(y) + "\n"
		fp.write(data)
	fp.close()

def load_four():
	dict5 = {}
	list5 =[]
	fp3 = open("Desktop/highscores_function_four.txt", "r")
	for line in fp3:
		list6 = line.split(",")
		print(list6[0],":",list6[1])
		dict5[list6[0]] = list5
	fp3.close()
	return dict5


def save_eight(dict_eight):
	fp = open("Desktop/highscores_function_eight.txt","a")
	for x,y in dict_eight.items():
		data = x + ", " + str(y) + "\n"
		fp.write(data)
	fp.close()


def load_eight():
	dict10 = {}
	list10 = []
	fp = open("Desktop/highscores_function_eight.txt", "r")
	for line in fp:
		list11 = line.split(",")
		print(list11[0],":",list11[1])
		dict10[list11[0]] = list10
	fp.close()
	return dict10
