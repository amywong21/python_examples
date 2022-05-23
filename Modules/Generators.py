# Vorteil vom generator ist, dass nur die elemente generiert werden die man anfragt.
# Generator in Crawler einbauen
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

		yield CrawledArticle(title, emoji, content, image)

		next_button = doc.select_one(".navigation .btn")
		if next_button:
			next_href = next_button.attrs["href"]
			next_href = urljoin(url, next_href)            
			url = next_href
		else:
			url = ""

import csv
def article_fetcher_with_generator():	
	fetcher = ArticleFetcher()

	with open('crawler_output.csv', 'w', newline='', encoding='utf16') as csvfile:
		articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		counter = 0
			
		for article in fetcher.fetch():
			if counter == 8:
				break
			counter = counter + 1
			print(article.emoji + ": " + article.title)
			articlewriter.writerow([article.emoji, article.title, article.image, article.content])

	print("Programmende")

#######################################################

def gen_generator():
	for i in range(0, 10):
		print("gen: " + str(i))
		yield i

def process_complete_list():
	for element in gen_list():
		print("print: " + str(element))


def gen_list():
	liste = []
	for i in range(0, 10):
		print("gen: " + str(i))
		liste.append(i)
	# ohne return gibt es einen Fehler: 
	# TypeError: 'NoneType' object is not iterable
	return liste

def example_generator():
	# Ohne generator:
	# Schleife um alle Listen Elemente zu erzeugen
	# Zweite Schleife um dann alle Listen Elemente zu Printen
	# Gesamte Liste muss erst angelegt werden, um dann verarbeitet zu werden
	process_complete_list()
	
	# Mit generator
	# Direkt nach dem erzeugen eines Elementes der Liste in gen_generator(), 
	# erfolgt die Weitergabe an die verarbeitende Schleife per yield
	for element in gen_generator():
		if element == 4:
			print("break")
			break
		print("print: " + str(element))

	for element in gen_generator():
		print("print: " + str(element))

	print("Programmende")


