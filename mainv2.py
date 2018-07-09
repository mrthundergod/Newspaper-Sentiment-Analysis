from main import *

def startMenu():
  mainCategories = ['https://www.thehindu.com/news/national/?page=','https://www.thehindu.com/news/international/?page=',
  'https://www.thehindu.com/sci-tech/science/?page=','https://www.thehindu.com/business/?page=']


  statesCategories = ['https://www.thehindu.com/news/national/kerala/?page=','https://www.thehindu.com/news/national/tamil-nadu/?page=','https://www.thehindu.com/news/national/karnataka/?page=','https://www.thehindu.com/news/national/andhra-pradesh/?page=','https://www.thehindu.com/news/national/telangana/?page=']

  print('\nHello! Welcome to the News Reader and Analysis App!\nSelect from the following Categories.\n 1. National News. \n 2. International News. \n 3. State News. \n 4. Science News. \n 5. Business News')

  checkCategory = input()

  if checkCategory == '1':
    mainUrl = mainCategories[0]
  elif checkCategory == '2':
    mainUrl = mainCategories[1]
  elif checkCategory == '3':
    print('\nSelect which District to view:\n 1. Kerala. \n 2. Tamil Nadu.\n 3. Karnataka.\n 4. Andra Pradesh.\n 5. Telungana.\n')

    selectDistrict = input()

    if selectDistrict == '1':
      mainUrl = statesCategories[0]
    elif selectDistrict == '2':
      mainUrl = statesCategories[1]
    elif selectDistrict == '3':
      mainUrl = statesCategories[2]
    elif selectDistrict == '4':
      mainUrl = statesCategories[3]
    elif selectDistrict == '5':
      mainUrl = statesCategories[4]
    else:
      print("Try again!!!")

  elif checkCategory == '4':
    mainUrl = mainCategories[2]
  elif checkCategory == '5':
    mainUrl = mainCategories[3]
  else:
    print("Try Again!!")

  return mainUrl

if __name__=='__main__':
	lists=[]
	mainUrl = startMenu()
	print("\n HELLO!!! What do you wanna do know? : \n 1. See News \n 2. See Sentiment Value for National News \n 3. See overall Sentiment for now. \n")
	check = input("Enter the number: ")
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
