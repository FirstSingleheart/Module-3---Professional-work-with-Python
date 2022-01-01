import requests
import bs4


KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Программирование', 'IT-компании'}

HEADERS = {'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
          'Accept-Language': 'ru-RU,ru;q=0.9',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'Cache-Control': 'max-age=0',
          'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
          'sec-ch-ua-mobile': '?0'
}

responce = requests.get("https://habr.com/ru/all/", headers=HEADERS)
responce.raise_for_status()

text = responce.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')


def get_news():
    for article in articles:
        date = article.find('span', class_='tm-article-snippet__datetime-published')
        time = date.time['title']
        hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
        hubs = set(hub.find('span').text for hub in hubs)
        title = article.find('a', class_='tm-article-snippet__title-link')
        href = title['href']
        url = 'https://habr.com' + href
        title_span = title.find('span').text
        if KEYWORDS & hubs:
            print(time, ' - ', title_span, url)
            print("*****")


if __name__ == '__main__':
    get_news()