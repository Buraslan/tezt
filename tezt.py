from bs4 import BeautifulSoup #pip install beautifulsoup4
import requests #pip install requests
import urllib
import time
import random


def looper():
    url1 = "https://www.vatanbilgisayar.com/sony-playstation-5-oyun-konsolu-ve-hfw-oyunu.html"
    url2 = "https://www.amazon.com.tr/dp/B0BM7PSRBR/" 

    print("Playstation 5 taraması başladı...")
    print("Gün içinde @indirim_firsat_dunyasi telegram kanalını takip edin...")
    while True:
        time.sleep(random.randint(3,10))
        print("Taranıyor...")
        



def main():
    looper()
    


if __name__ == "__main__":
    main()

