#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    description = soup.find_all('meta', attrs={'property':'og:description'})

    for i in description:
        description = i["content"]

    image = soup.find_all('meta', attrs={'property':'og:image'})

    for i in image:
        image = i["content"]

    text = ""
    for i in soup.find_all('p'):
        text += i.get_text()

    return url, title, description, image, text
