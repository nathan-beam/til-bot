from bs4 import BeautifulSoup
import urllib3
import sqlite3

def pull_facts():
	http = urllib3.PoolManager()

	url = "https://en.wikipedia.org/wiki/Main_Page"
	response = http.request('GET', url)
	soup = BeautifulSoup(response.data, "html.parser")

	dyk = soup.find(id="mp-dyk")

	db = sqlite3.connect('facts.db')

	for li in dyk.ul.find_all("li"):
		title = li.text.replace("?","").replace("...","TIL")
		link = "https://en.wikipedia.org"+li.b.a.get("href")
		db.cursor().execute("INSERT INTO facts VALUES(?,?)",[title,link])
		db.commit()
		print(title)

pull_facts()