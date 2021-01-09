import os
import requests
from bs4 import BeautifulSoup

class MobileCrawler:


	##ISSUES
	#mobile.de needs cookies enabled browser request

	#cBox-body cBox-body--resultitem dealerAd rbt-reg rbt-no-top
	url=""

	def __init__(self):
		self.url="https://suchen.mobile.de/fahrzeuge/search.html?c=MobileHome&c=VanMotorhome&cn=DE&con=USED&emc=EURO5&ems=EMISSIONSSTICKER_GREEN&ft=DIESEL&ft=PETROL&isSearchRequest=true&p=%3A30000&s=Motorhome&sfmr=false&vc=Motorhome"
  
	def crawlMobile(self, url):
		carList=[]
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'lxml')
		print(soup)
		cars=soup.find_all(class_='g-row')
  		
		print(cars)
  


