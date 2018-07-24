from textblob import TextBlob                                                   # the module that runs sentiment analysis             
from pageScraper import *                                                       # import all functions from pageScraper

def newsAnalysis(dataDiX):                                                      # take the { title:story } dictionary and runs sentiment
    sent = []                                                                   # analysis on it and returns 
    sentVal = []
    for news in list(dataDiX.values()):
      analysis = TextBlob(news)
      sentiment = find_Sentiment(analysis.sentiment.polarity)
      qq = analysis.sentiment.polarity
      sentVal.append(qq)
      sent.append(sentiment)
    return sent, sentVal

def find_Sentiment(val):                                                                                                               
    if val<=0.1 and val>-0.1:
        return 'Neutral'
    elif val>0.1:
        return 'Positive'
    else:
        return 'Negative'

def listMaker(newsPaper, titles, sent, sentVal, lists):
  totalSent = 0
  for i in range(len(newsPaper)):
    sas = titles[i] + ' : ' + sent[i]+ ' : ' + str(sentVal[i])
    totalSent+=sentVal[i]
    lists.append(sas)
    lists= [x.replace('\n', '') for x in lists]
  return lists, totalSent
         
def sentimentAnalysis(newsPaper, titles, links):
  lists = []
  stories = newsStoryGrabber(links)
  newsPaper=dict(zip(titles,stories))
  sent, sentVal = newsAnalysis(newsPaper)
  lists, totalSent = listMaker(newsPaper, titles, sent, sentVal, lists)
  for i in range(len(newsPaper)):
    print(lists[i])

def avgSentiment(newsPaper, titles, links):
  lists = []
  stories = newsStoryGrabber(links)
  newsPaper=dict(zip(titles,stories))
  sent, sentVal = newsAnalysis(newsPaper)
  lists, totalSent = listMaker(newsPaper, titles, sent, sentVal, lists)

  avgSent = totalSent/len(titles)
  #print("Average Sentiment now , is : "+ str(avgSent))
  return avgSent

if __name__=='__main__':
  check =input("1. Sentiment Analysis\n2. Average Sentiment\n")
  lists=[]
  mainUrl = 'https://www.thehindu.com/news/national/?page='
  newsPaper={}
  sentValue=[]
  for x in range(1,6):
    url = urlMaker(mainUrl, x)
    soup = soupee(url)
    titles, links = parser(soup)
    if check == '1':
      sentimentAnalysis(newsPaper, titles, links)
    else:
      avgSentVal = avgSentiment(newsPaper, titles, links)
      sentValue.append(avgSentVal)

  if check== '2':
    print("Average Sentiment now is : "+ str(sum(sentValue)))




    
    
    

