import requests
from bs4 import BeautifulSoup
import os

domain = ("https://www.youtube.com")
search_par = ("/results?search_query=")
search = ("vsauce")

links = []
titles = []

assembled_url = (domain + search_par + search)
html_status = requests.get(assembled_url)
soup = BeautifulSoup(html_status.content, "html.parser")
video_links = soup.find_all("a", class_ = "yt-uix-tile-link")
print(video_links)
for i in video_links:
	href = i.get("href")
	final_url = (domain + href)
	title = i.get("title")
	print(title)
	print(final_url)