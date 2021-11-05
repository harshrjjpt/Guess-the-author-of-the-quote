import requests
from bs4 import BeautifulSoup
import csv
from random import choice
import pyfiglet
from termcolor import colored 
from colorama import init
init()

samaan = []
main_url ="https://quotes.toscrape.com/"
url = "/page/1/"

while url:
	response = requests.get(f"{main_url}{url}")
	scrapping_line = f"Now Scraping {main_url}{url}"
	colorplate = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
	print(colored(scrapping_line, color=choice(colorplate)))
	soup = BeautifulSoup(response.text, "html.parser")
	datas = soup.find_all(class_="quote")

	for data in datas:
		samaan.append({
			"quotes": data.find(class_="text").get_text(),
			 "author": data.find(class_="author").get_text(),
			 "link": data.find("a")["href"]
			 })
	nextb = soup.find(class_="next")
	url = nextb.find("a")["href"] if nextb else None



reply = "Who Said This Quote "
result = pyfiglet.figlet_format(reply, font="slant")
print(colored(result, color="green"))

name = input(f"What is your name? ")

def start_game():

	print(f"Hello!! {name} I will show you a random quote \n You have to answer the person who said that quote")
	answer = input(f"So shall we start?:  ")
	guess = 3
	if answer == "yes" or answer == "y" or answer == "okay" or answer == "ok":
		baat = choice(samaan)
		print("Here's the quote :")
		print(colored(baat["quotes"], color="cyan"))
	else:
		quit()
	write_answer = input()
	congrats = "Congrats!!your answer is correct"
	no_congrats = "sorry , your guess is wrong"
	if write_answer.lower() == baat["author"].lower():
		print(colored(congrats, color="green"))
		quit()
	else: 
		print(colored(no_congrats, color="red"))
		guess -= 1
		print(f"{guess} guesses remaining")
		print("Here's a hint :")
		hint_1 = baat["author"][0]
		print(f"the name of the author starts from {hint_1}")

	write_answer2 = input()
	if write_answer2.lower() == baat["author"].lower():
		print(colored(congrats, color="green"))
		quit()
	else:
		print(colored(no_congrats, color="red"))
		guess -= 1
		print(f"{guess} guesses remaining")
		print("Here's another hint :")
		imp = requests.get(f"{main_url}{baat['link']}")
		soup = BeautifulSoup(imp.text, "html.parser")
		birth_date = soup.find(class_="author-born-date").get_text()
		birth_location = soup.find(class_="author-born-location").get_text()
		description = soup.find(class_="author-description").get_text()
		print(f"The Author was born on {birth_date} {birth_location}")

	write_answer3 = input()
	if write_answer3.lower() == baat["author"].lower():
		print(colored(congrats, color="green"))
		quit()
	else:
		print(colored(no_congrats, color="red"))
		guess -= 1
		print(f"The name of the Author is: ")
		print(baat["author"])
		print(description)

	game = "GAME-OVER"
	game_over = pyfiglet.figlet_format(game, font="slant")
	print(colored(game_over, color="cyan"))
	playagain = ""
	while playagain.lower() not in ("yes", "y", "no", "n"):
	    playagain = input(f"Do yo want to play again??(y/n) : ")
	if playagain.lower() in ("yes", "y"):
		start_game()
	elif playagain.lower() in ("no", "n"):
		print("Okay, Bye")
		quit()

start_game()	