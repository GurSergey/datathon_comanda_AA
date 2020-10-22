from urllib.request import Request
from lxml import html
import os
import shutil

IMAGES_FOLDER_NAME = './images'
START_URL = 'https://lapkins.ru/cat/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
import urllib.request
req = urllib.request.Request(START_URL, headers=HEADERS)
start_page=urllib.request.urlopen(req).read()
start_page=html.fromstring(start_page)
# Словарь - название породы-ссылка
start='https://lapkins.ru'
cats={breed:start+url+"photo/" for breed,url in
      zip(start_page.xpath('//div[contains(@class,"pop-porodi-block")]/a/span/text()'),start_page.xpath('//div[contains(@class,"pop-porodi-block")]/a/@href'))}
# Реализуем полный проход по всем породам
root_cats=os.getcwd()+os.sep+"Cats_lapkins"
if os.path.isdir(root_cats):
    shutil.rmtree(root_cats)
os.mkdir(root_cats)
print("Всего на сайте пород:  " + str(len(cats.items())))
for breed_name,url_breed in cats.items():
    print("Загружается: " + breed_name)
    req = urllib.request.Request(url_breed,headers=HEADERS)
    breed_page=urllib.request.urlopen(req).read()
    breed_page=html.fromstring(breed_page)
    #img_urls=breed_page.xpath('//figure[contains(@class,"wp-block-image")]/img/@data-lazy-src')
    img_urls=[start+x for x in breed_page.xpath('//div[contains(@data-pagen,"more-photo")]/div[contains(@class,"foto-img")]/a/@href')]
    num_img=1
    # Работа с папками - если есть, удаляем, если нет, то создаем
    breed_path=root_cats + os.sep + breed_name
    os.mkdir(breed_path)
    for url in img_urls:
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent','Mozilla/5.0')
        opener.retrieve(url, breed_path + os.sep + breed_name + " " + str(num_img) + '.jpg')
        num_img += 1
 
