from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




class MobileCrawler:


	##ISSUES
	#mobile.de needs cookies enabled browser request

	#cBox-body cBox-body--resultitem dealerAd rbt-reg rbt-no-top
	url=""
	

	def __init__(self):
		self.url="https://suchen.mobile.de/fahrzeuge/search.html?c=MobileHome&c=VanMotorhome&cn=DE&con=USED&emc=EURO5&ems=EMISSIONSSTICKER_GREEN&ft=DIESEL&ft=PETROL&isSearchRequest=true&p=%3A30000&s=Motorhome&sfmr=false&vc=Motorhome"
		

	def crawlMobile(self, url):
		carList=[]
		driver=webdriver.Chrome("/Users/doed/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver")
		driver.get(url)
		element=driver.find_element_by_xpath('//*/div[4]/div/div[3]/div[4]/div[2]/div[1]/div[16]')
		print(element.text)



			#class="cBox-body cBox-body--resultitem dealerAd rbt-reg rbt-no-top"

  


