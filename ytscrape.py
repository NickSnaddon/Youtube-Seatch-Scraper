import requests
from bs4 import BeautifulSoup
import os
import pytube
import sys

domain = ("https://www.youtube.com")
search_par = ("/results?search_query=")
links = []
titles = []
txt = False
video = False


def search_term():
	user_in = input("> ")
	l = []
	for i in user_in:
		if i == " ":
			l.append("+")
		else:
			l.append(i)
	final = "".join(l)
	scrape(final)

def options():
	global video
	global txt
	i = 0
	while i != "3":
		print("Toggle scraping") 
		print("--------------------")
		print("1. Video")
		print("2. Text")
		print("3. Exit")
		i = input("> ")
		if i == "1":
			if video == True:
				video = False
				print("Video downloading is OFF")
				print("--------------------")
				continue
			else:
				video = True
				print("Video downloading is ON")
				print("--------------------")
				continue
		elif i == "2":
			if txt == True:
				txt = False
				print("Text downloading is OFF")
				print("--------------------")
				continue
			else:
				txt = True
				print("Text downloading is ON")
				print("--------------------")
				continue
		elif i == "3":
			break

def main_menu():
	while True:
		print("1. Scrape")
		print("2. Options")
		print("3. Exit")
		i = input("> ")
		if i == "1":
			search_term()
		elif i == "2":
			options()
		elif i == "3":
			sys.exit()

def scrape(search):
	assembled_url = (domain + search_par + search)
	html_status = requests.get(assembled_url)
	soup = BeautifulSoup(html_status.content, "html.parser")
	video_links = soup.find_all("a", class_ = "yt-uix-tile-link")
	for i in video_links:
		href = i.get("href")
		final_url = (domain + href)
		title = i.get("title")
		print(title)
		print(final_url)

main_menu()


