import os
from GoogleImageScraper import GoogleImageScraper
import pyautogui

def GoogleImage():
    oo = open('D:\\How To Make Jravis In Python\\DataBase\\webdriver\\Data.txt','rt')
    query = str(oo.read())
    oo.close()
    pppp = open('D:\\How To Make Jravis In Python\\DataBase\\webdriver\\Data.txt','r+')
    pppp.truncate(0)
    pppp.close()

    webdriver = "D:\How to make jravis in python\DataBase\webdriver.exe"
    photos = "D:\How to make jravis in python\GoogleImageScrapper-0.1.0\GoogleImageScrapper"

    search_keys = [f"{query}"]
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)

    for search_key in search_keys:
        image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)

    os.startfile(photos)

GoogleImage()
