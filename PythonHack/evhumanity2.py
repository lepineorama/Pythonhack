from sys import exit
from random import randint

prompt_1 = "What really killed the dinosaurs? "
prompt_2 = "Next on ESPN2: The World Series of ... "
prompt_3 = "The class field trip was completely ruined by ... "
prompt_4 = "I get by with a little help from ... "
prompt_5 = "Instead of coal, Santa now gives the bad children ... "
prompt_6 = "Introducing X-treme Baseball! It's like baseball, but with ... "
prompt_7 = "Why can't I sleep at night? "
prompt_8 = "What did Vin Diesel eat for dinner? "
prompt_9 = "The fault, dear Brutus, is not in our stars, but in ... "
prompt_10 = "What's my secret power? "

ansfile = open("answers.txt")


def play_again():
	print("Play again (Y/N)?")

	choice = input("> ")

	if choice == "Y" or choice == "y":
		return True
	elif choice == "N" or choice == "n":
		return False


def start():
	print("Welcome to Eggplants Against Humanity")
	print("""MMMMMMMMMMMMMMMMMMMMMMMMMMWXK0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMXkddkXWMN00KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWN0xdONXkdddx0KXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMN0000KKKKXKxdddddddxOXWMWNXK0KNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWKxodddddkOkddddddddddkKKOxdddxKMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXkodddddddddoddddddoodxddddddd0WMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMN0xdddddddddddddddddddddddddddONMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWNXK0OkxddddxkkkxddddddddxkkkxdddddkKNWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWX0kxdddddddk0OOOOOOOOOOOOOOOOOOO00kddddxk0KNWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNOddddddddx0KOdoooooddxxxdddoooood0KOdddddodxOXWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWKkdddddx0KxooooooooooooooooooooookK0dddddddxKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMN0kxdxKKxooooooooooooooooooooooookK0ddddk0NWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMW0xx0KxooooooooooooooooooooooooookXOdx0NWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMW0xdOXkooooollloooooooooooolllooood0KkdxXWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMW0doxK0doooc;,cdlcooooooooc;':dlloooxK0ddkXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWKxddOXkoool,..;c;;looooool,..;c;;looo0XOxOXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWNKKXNXxoool:'...':oooooool:'...':ooookNWWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMKdoooooc::clooooooooolc:::loooooxXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMKdoooooc;coooooooooooool::loooooxXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXxoooool;,:looooooooooc;,:loooookNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWOoooooolc;;;:ccccc::;,;coooooodKWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNOoooooooll::;;;;;;:cloooooood0WMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMW0xooooooooooooooooooooooookKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNKkdooooooooooooooooooxOKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0kxxddddddddxkO0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXXXNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")
	print("A rather silly game of prompts and answers")
	prompt()

	answer = play_again()
	while answer == True: 
		print("Playing again")
		prompt()
		answer = play_again()
	print("Thanks for playing!")

def prompt():	
	print("Pick a prompt (1-10)")

	choice = input("> ")

	if choice == "1":
		opt = prompt_1
		print(prompt_1)
		the_end = answer()
		print(opt + the_end)
	elif choice == "2":
		opt = prompt_2
		print(prompt_2)
		the_end = answer()
		print(opt + the_end)
	elif choice == "3":
		opt = prompt_3
		print(prompt_3)
		the_end = answer()
		print(opt + the_end)
	elif choice == "4":
		opt = prompt_4
		print(prompt_4)
		the_end = answer()
		print(opt + the_end)
	elif choice == "5":
		opt = prompt_5
		print(prompt_5)
		the_end = answer()
		print(opt + the_end)
	elif choice == "6":
		opt = prompt_6
		print(prompt_6)
		the_end = answer()
		print(opt + the_end)
	elif choice == "7":
		opt = prompt_7
		print(prompt_7)
		the_end = answer()
		print(opt + the_end)
	elif choice == "8":
		opt = prompt_8
		print(prompt_8)
		the_end = answer()
		print(opt + the_end)
	elif choice == "9":
		opt = prompt_9
		print(prompt_9)
		the_end = answer()
		print(opt + the_end)
	elif choice == "10":
		opt = prompt_10
		print(prompt_10)
		the_end = answer()
		print(opt + the_end)
	else:
		print("This value must be a number, dude.")

def shorten(answers, hand_count):
	hand_rand = []
	for i in range(hand_count):
		answer = answers[randint(0, 29)]
		while answer in hand_rand:
			answer = answers[randint(0, 29)]
		hand_rand.append(answer)
	return hand_rand


def get_answers():
	ansfile = open("answers.txt")
	answers = []	
	for i in range(30):
		ans_lines = ansfile.readline()
		answers.append(ans_lines)

	hand_rand = shorten(answers, 5)
	return hand_rand


def answer():
	answer_array = get_answers()	
	print("Pick an answer (1-5)")
	i = 1
	for ans in answer_array:
		print(f"{i}. {ans}")
		i += 1

	choice = int(input("> "))

	fini = answer_array[choice - 1]
	return fini

start()