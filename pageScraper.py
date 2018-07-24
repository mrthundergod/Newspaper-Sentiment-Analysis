import lxml, urllib.request                                                 # lxml is a library for parsing, urllib is to open the page
from bs4 import BeautifulSoup as bs                                         # bs4 helps decode and search through page.

def urlMaker(mainUrl,x):                                                    # For making individual page URLS
  url = mainUrl + str(x)
  return url

def soupee(url):                                                            # Create Soup object with bs4
  sauce=urllib.request.urlopen(url)
  soup = bs(sauce, 'lxml')
  return soup

def parser(soup):                                                           # Parse page and create two lists of the titles and link
  titles = []                                                               # to each news of title
  links = []
  for news in soup.find_all('div', class_='story-card-news'):
    title = news.h3.text
    link = news.find_all('a')
    titles.append(title)
    links.append(link[2]['href'])
  return  titles, links

def newsStoryGrabber(links):                                                # Use the Links list to goto the site and get the first two
  data=[]                                                                   # paragraphs of the new and return a story list.
  for i in range(len(links)):
    url = links[i]
    sauce=urllib.request.urlopen(url)
    soup = bs(sauce, 'lxml')
    aa = soup.find('div', class_='article')
    bb = aa.find_all('p')
    cc = bb[1].text + bb[2].text
    data.append(cc)
  return data

def seeNews(titles,links):                                                  # Show each story with title as the indices of each correspond 
  stories = newsStoryGrabber(links)                                         # correctly, i.e. index zero of both are for same News.
  for i in range(len(titles)):
    print(titles[i] + '\n' + stories[i]+ ' \n')
    print('________________________________________\n')


if __name__=='__main__':                                                    # Main function
  lists=[]
  mainUrl = 'https://www.thehindu.com/news/national/?page='                 # Just the National Page           
  print("")

  for x in range(1,6):                                                      # Iterate through first 6 pages
    newsPaper={}
    url = urlMaker(mainUrl, x)
    soup = soupee(url)
    titles, links = parser(soup)
    seeNews(titles,links)
