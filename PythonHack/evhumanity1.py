from sys import exit

prompt_1 = "What really killed the dinosaurs?"
prompt_2 = "Next on ESPN2: The World Series of ..."
prompt_3 = "The class field trip was completely ruined by ..."
prompt_4 = "I get by with a little help from ..."
prompt_5 = "Instead of coal, Santa now gives the bad children ..."

ans_1 = " Silence."
ans_2 = " Free samples."
ans_3 = " Authentic Mexican cuisine."
ans_4 = " An oversized lollipop."
ans_5 = " Sweet, sweet vengeance."


def play_again():
	print("Play again (Y/N)?")

	choice = input("> ")

	if choice == "Y" or choice == "y":
		return True
	elif choice == "N" or choice == "n":
		return False



def start():
	print("Welcome to Eggplants 2 Eggplants")
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
	print("Pick a prompt (1-5)")

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
	else:
		print("This value must be a number, dude.")

def answer():
	print("Pick an answer (1-5)")

	choice = input("> ")

	if choice == "1":
		fini = ans_1
		print(ans_1)
	elif choice == "2":
		fini = ans_2
		print(ans_2)
	elif choice == "3":
		fini = ans_3
		print(ans_3)
	elif choice == "4":
		fini = ans_4
		print(ans_4)
	elif choice == "5":
		fini = ans_5
		print(ans_5)
	else:
		print("What did we say about choosing a number???")
	return fini


start()