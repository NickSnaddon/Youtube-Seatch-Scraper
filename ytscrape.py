import requests
from bs4 import BeautifulSoup
import os
import pytube

domain = ("https://www.youtube.com")
search_par = ("/results?search_query=")
links = []
titles = []

def search_term(term):
	l = []
	for i in term:
		if i == " ":
			l.append("+")
		else:
			l.append(i)
	final = "".join(l)
	scrape(final)

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

i = input("> ")
search_term(i)

