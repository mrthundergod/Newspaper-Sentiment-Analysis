import lxml, urllib.request
from bs4 import BeautifulSoup as bs
from textblob import TextBlob
from pageScraper import *
from sentAnalysis import *


if __name__=='__main__':
	lists=[]
	print("\n HELLO!!! What do you wanna do know? : \n 1. See National News \n 2. See Sentiment Value for National News \n 3. See overall Sentiment for now. \n")

	check = input("Enter the number: ")
	mainUrl = 'https://www.thehindu.com/news/national/?page='
	sentValue=[]
	for x in range(1,3):
		newsPaper={}
		url = urlMaker(mainUrl, x)
		soup = soupee(url)
		titles, links = parser(soup)

		if check=='1':
			seeNews(titles,links)
		elif check=='2':
			sentimentAnalysis(newsPaper, titles, links)
		else:
			avgSentVal = avgSentiment(newsPaper, titles, links)
			sentValue.append(avgSentVal)
	if check== '3':
		avgSentiment = find_Sentiment(sum(sentValue))
		print("Average Sentiment now is : "+ avgSentiment+'. ('+str(sum(sentValue))+')')


    
    
    

