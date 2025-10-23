import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://lite.cnn.com/"  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    headlines = soup.find_all(class_="card--lite")
    with open("headlines.txt", "w") as file:
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                file.write(text + "\n")

if __name__ == "__main__":
    scrape_headlines()
