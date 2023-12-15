# real_python_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_real_python():
    url = 'https://realpython.com/tutorials/python/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='card border-0 mb-4')

        top_articles = []
        for article in articles:
            title = article.find('h2', class_='card-title').text.strip()
            link = article.find('a')['href']
            
            top_articles.append({
                'title': title,
                'link': link
            })

        return top_articles
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    top_python_articles = scrape_real_python()

    if top_python_articles:
        print("Top Python Articles on Real Python:")
        for idx, article in enumerate(top_python_articles, start=1):
            print(f"{idx}. {article['title']}")
            print(f"   Link: {article['link']}\n")
    else:
        print("Scraping failed.")
