# Ergebnisse als CSV speichern
# Jetzt haben wir den ArticleFetcher schon so angepasst, 
# dass er die Daten aus allen Seiten extrahiert. Aber eigentlich wäre es cool, 
# wenn er die Daten direkt als .csv-Datei speichern würde ;)

# Schaue dir das Modul csv an, und zwar die writer-Funktion:
# [https://docs.python.org/3/library/csv.html#csv.writer](https://docs.python.org/3/library/csv.html#csv.writer).
# - Passe dann den Ausgabe-Code so an, dass statt der Ausgabe hier im
# Notebook eine .csv-Datei gespeichert wird. Verwende als Spaltentrenner
# (Separator) ein Semikolon und als "quotechar" die doppelten
# Anführungszeichen ('"'); dann können wir die Datei später noch mit Excel öffnen.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class CrawledArticle():
	def __init__(self, title, emoji, content, image):
		self.title = title
		self.emoji = emoji
		self.content = content
		self.image = image
		
class ArticleFetcher():
	def __init__(self):
		self.articles = []
	
	def fetch(self):
		url = "http://python.beispiel.programmierenlernen.io/index.php"
		
		while url != "":
			print(url)
			time.sleep(0.2)
			r = requests.get(url)
			doc = BeautifulSoup(r.text, "html.parser")
			
			for card in doc.select(".card"):
				emoji = card.select_one(".emoji").text
				content = card.select_one(".card-text").text
				title = card.select(".card-title span")[1].text
				image = urljoin(url, card.select_one("img").attrs["src"])

				crawled = CrawledArticle(title, emoji, content, image)
				self.articles.append(crawled)

			next_button = doc.select_one(".navigation .btn")
			if next_button:
				next_href = next_button.attrs["href"]
				next_href = urljoin(url, next_href)            
				url = next_href
			else:
				url = ""
	
	def getArticles(self):
		return self.articles

import csv

def example_crawler_csv():
	fetcher = ArticleFetcher()
	with open('articles.csv', 'w', newline='', encoding='utf16') as csvfile:
		articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		fetcher.fetch()
		articles = fetcher.getArticles()
		
		for article in articles:
			articlewriter.writerow([article.emoji, article.title, article.image, article.content])
		