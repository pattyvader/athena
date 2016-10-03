from bs4 import BeautifulSoup

def extract_data(html):
    data = {}

    soup = BeautifulSoup(html)

    title = soup.find_all('meta', attrs={'property':'og:title'})

    for i in title:
        title = i["content"]

    url = soup.find_all('meta', attrs={'property':'og:url'})

    for i in url:
        url = i["content"]

    return url, title
