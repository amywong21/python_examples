# Passe den ArticleFetcher so an, dass er die Informationen aus allen Seiten extrahiert.
# Hier nochmal die URL: [http://python.beispiel.programmierenlernen.io/index.php](http://python.beispiel.programmierenlernen.io/index.php)
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
		articles = []
		
				# solange es eine gültige Url gibt
		while url != "": 
			print(url)
			print("\n")
			# langsam genug für den Server sein, 
			# damit man nicht als Angreifer gesperrt wird 
			time.sleep(1)
			# parser geht durch response Text durch und 
			# baut ein HTML Dokument auf (doc)
			response = requests.get(url)
			doc = BeautifulSoup(response.text, "html.parser")

			# Element (hier Artikel) selektieren -> <div class="card">            
			for card in doc.select(".card"):
				emoji = card.select_one(".emoji").text
				content = card.select_one(".card-text").text
				title = card.select(".card-title span")[1].text
				image_url = urljoin(url, card.select_one("img").attrs["src"])

				# rufe def __init__(self, title, emoji, content, image_url):
				crawled = CrawledArticle(title, emoji, content, image_url)

				articles.append(crawled)

			next_button = doc.select_one(".navigation .btn")
			if next_button:
				next_href = next_button.attrs["href"]
								# kombiniere Basis Url mit dem Link 
								# der in dem Button hinterlegt ist  
				next_href = urljoin(url, next_href)
				url = next_href 
			else:
				url = ""
		
		return articles

def example_crawler():
	print("\n")
	fetcher = ArticleFetcher()
	for article in fetcher.fetch():
		print(article.emoji + ": " + article.title)