import requests
import pyquery
import sys

host = 'https://en.wikipedia.org'
url = host + '/wiki/'

headers = {
    'user-agent': (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    ),
}


class WikipediaPage(object):
    def __init__(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image
        
def lookup_on_wikipedia(page_name):
    html = get_response_text(page_name)
    return get_page_from_response_html(html)

def get_response_text(page_name):
    response = requests.get(url + page_name, headers=headers)
    response.raise_for_status()
    return response.text
    
def get_page_from_response_html(html):
    doc = pyquery.PyQuery(html)
    # get the title and first paragraph
    title = doc('#firstHeading').text()
    first_paragraph = doc('#mw-content-text p').eq(0).text()
    # get the url of the first image on the page
    first_image = doc('#mw-content-text img').eq(0)
    image_url = first_image.parent()[0].attrib['href']
    # make it absolute if it is relative
    if image_url.startswith('/'):
        image_url = host + image_url
    return WikipediaPage(title, first_paragraph, image_url)
    
def lookup_and_print(page_name):
    page = lookup_on_wikipedia(page_name)
    print(page.title, page.description, page.image, sep='\n')
    
lookup_and_print("Data_analytics")
