import lxml, urllib.request
from bs4 import BeautifulSoup as bs

def urlMaker(mainUrl,x):
  url = mainUrl + str(x)
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

def seeNews(titles,links):
  stories = newsStoryGrabber(links)
  for i in range(len(titles)):
    print(titles[i] + '\n' + stories[i]+ ' \n')
    print('________________________________________\n')


if __name__=='__main__':
  lists=[]
  mainUrl = 'https://www.thehindu.com/news/national/?page='
  print("")

  for x in range(1,6):
    newsPaper={}
    url = urlMaker(mainUrl, x)
    soup = soupee(url)
    titles, links = parser(soup)
    seeNews(titles,links)