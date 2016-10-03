#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def extract_data(html):
    url = extract_url(html)
    title = extract_title(html)
    description = extract_description(html)
    image = extract_image(html)
    text = extract_text(html)

    return url, title, description, image, text

def extract_url(html):
    soup = BeautifulSoup(html)
    url = soup.find_all('meta', attrs={'property':'og:url'})

    for i in url:
        return i["content"]

def extract_title(html):
    soup = BeautifulSoup(html)
    title = soup.find_all('meta', attrs={'property':'og:title'})

    for i in title:
        return i["content"]

def extract_description(html):
    soup = BeautifulSoup(html)
    description = soup.find_all('meta', attrs={'property':'og:description'})

    for i in description:
        return i["content"]

def extract_image(html):
    soup = BeautifulSoup(html)
    image = soup.find_all('meta', attrs={'property':'og:image'})

    for i in image:
        return i["content"]

def extract_text(html):
    text = ""
    soup = BeautifulSoup(html)

    for i in soup.find_all('p'):
        text += i.get_text()

    return text
