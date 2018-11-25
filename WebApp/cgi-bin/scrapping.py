#!C:/Program Files/Python37/python.exe

import urllib.request as url
import bs4


def getReviews(movie_name):
    website = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + movie_name+ "&s=all"
    url1 = url.urlopen(website)
    soup = bs4.BeautifulSoup(url1, 'lxml')
    data = soup.findAll('td', class_='result_text')
    data1 = data[0].a['href']
    website_1 = "https://www.imdb.com/" + data1
    url2 = url.urlopen(website_1)
    soup1 = bs4.BeautifulSoup(url2, 'lxml')
    data2 = soup1.find('div', class_='user-comments')
    data3 = data2.findAll('a')[-1]['href']
    website_2 = "https://www.imdb.com"+ data3
    url3 = url.urlopen(website_2)
    soup3 = bs4.BeautifulSoup(url3,'lxml')
    reviews = soup3.findAll('div',class_='text show-more__control')

    review_list = []
    for review in reviews:
        review_list.append(review.get_text())
    return review_list

