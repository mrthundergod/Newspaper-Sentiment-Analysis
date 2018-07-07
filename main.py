import lxml, urllib.request
from bs4 import BeautifulSoup as bs
from textblob import TextBlob

def urlMaker(x):
  url = 'https://www.thehindu.com/news/national/?page='+str(x)
  return url

def soupee(url):
  sauce=urllib.request.urlopen(url)
  soup = bs(sauce, 'lxml')
  return soup

def parser(soup):
  titles = []
  links = []
  for news in soup.find_all('div', class_='story-card-news'):
    title = news.h3.text
    link = news.find_all('a')
    titles.append(title)
    links.append(link[2]['href'])
  return  titles, links

def newsStoryGrabber(links):
  data=[]
  for i in range(len(links)):
    url = links[i]
    sauce=urllib.request.urlopen(url)
    soup = bs(sauce, 'lxml')
    aa = soup.find('div', class_='article')
    bb = aa.find_all('p')
    cc = bb[1].text + bb[2].text
    data.append(cc)
  return data

def find_Sentiment(val):
    if val<=0.1 and val>-0.1:
        return 'Neutral'
    elif val>0.1:
        return 'Positive'
    else:
        return 'Negative'

def newsAnalysis(dataDiX):
    sent = []
    sentVal = []
    for news in list(dataDiX.values()):
      analysis = TextBlob(news)
      sentiment = find_Sentiment(analysis.sentiment.polarity)
      qq = analysis.sentiment.polarity
      sentVal.append(qq)
      sent.append(sentiment)
    #df = pd.DataFrame(data)
    return sent, sentVal

def listMaker(newsPaper, titles, dic, sentVal, lists):
  for i in range(len(newsPaper)):
    sas = titles[i]+' : '+ dic[i]+' : '+str(sentVal[i])
    lists.append(sas)
    lists= [x.replace('\n', '') for x in lists]
  return lists

def seeNews(titles,links):
  stories = newsStoryGrabber(links)
  for i in range(len(titles)):
    print(titles[i] + '\n' + stories[i]+ ' \n')
    print('________________________________________\n')
         
def sentimentAnalysis(newsPaper, titles, lists):
  stories = newsStoryGrabber(links)
  newsPaper=dict(zip(titles,stories))
  dic, sentVal = newsAnalysis(newsPaper)
  lists = listMaker(newsPaper, titles, dic, sentVal, lists)
  print(lists)

def avgSentiment(titles,stories):
  newsPaper=dict(zip(titles,stories))
  dic, sentVal = newsAnalysis(newsPaper)
  


if __name__=='__main__':
  lists=[]

  print("\n HELLO!!! What do you wanna do know? : \n 1. See National News \n 2. See Sentiment Value for National News \n 3. See overall Sentiment for now. \n")
  
  check = input("Enter the number: ")

  for x in range(1,6):
    newsPaper={}
    url = urlMaker(x)
    soup = soupee(url)
    titles, links = parser(soup)

    if check=='1':
      seeNews(titles,links)
    elif check=='2':
      sentimentAnalysis(newsPaper, titles, lists)
    else:
      avgSentiment(titles,stories)


    
    
    

