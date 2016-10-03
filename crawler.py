import requests
import urllib2
import robotparser
from bs4 import BeautifulSoup
from urllib2 import URLError
from urllib2 import HTTPError
from urlparse import urlparse
from scraper import extract_data

url_seed = "https://www.python.org/"

def robot_txt(url):
    robot = robotparser.RobotFileParser()
    robot.set_url(url)
    robot.read()

    is_allowed = robot.can_fetch("*", url)

    return is_allowed

def is_allowed_url(domain,url):
    if domain in url:
        return True

    return False

def is_path_absolute(url):
    return bool(urlparse(url).netloc)

def get_links(html):
    try:
        soup = BeautifulSoup(html)
        link_list = []

        for links in soup.find_all('a', href=True):
            if not "#" in links['href']:
                link = links['href']

                domain_parse = urlparse(url_seed)
                domain = domain_parse.netloc

                if not is_path_absolute(links['href']):
                    link = domain + links['href']

                is_allowed_domain = is_allowed_url(domain,link)

                if is_allowed_domain:
                    if not link in link_list:
                        if not 'javascript' in link:
                            link_list.append(link)

        return link_list
    except (HTTPError,URLError) as e:
        print e
        pass

def get_html_page(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()

    return html

def main():
    is_allowed = robot_txt(url_seed)

    if is_allowed:
        list_links = []

        html_page = get_html_page(url_seed)
        list_links = get_links(html_page)

        for page in list_links:
            html = get_html_page("http://" + page)
            url, title, description = extract_data(html)

            #Extract data of the page and print in prompt
            print "URL:" + str(url)
            print "Title:" + str(title)
            print "Description:" + str(description) 
            print "--------------------------------"

if __name__ == "__main__":
    main()
