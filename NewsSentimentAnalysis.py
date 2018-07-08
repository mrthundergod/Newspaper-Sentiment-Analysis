from textblob import TextBlob
from PageScraper import *

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
         
def sentimentAnalysis(newsPaper, titles, lists):
  stories = newsStoryGrabber(links)
  newsPaper=dict(zip(titles,stories))
  dic, sentVal = newsAnalysis(newsPaper)
  lists = listMaker(newsPaper, titles, dic, sentVal, lists)
  print(lists)


if __name__=='__main__':
  lists=[]
  mainUrl = 'https://www.thehindu.com/news/national/?page='
  newsPaper={}
  
  for x in range(1,6):
    url = urlMaker(mainUrl, x)
    soup = soupee(url)
    titles, links = parser(soup)
    seeNews(titles,links)
    sentimentAnalysis(newsPaper, titles, lists)



    
    
    

