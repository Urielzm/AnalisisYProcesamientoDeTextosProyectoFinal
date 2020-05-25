from requests import get
from bs4 import BeautifulSoup

class Html2Text(object):
    def __init__(self, url=None):
        """
            Class constructor. Just needed URL to work. It's not necessary
            to create an instance of this class
        """
        self.URL = url

    def construct_headers(self, userAgent=None):
        """
            Method used to elaborate the HTTP headers to the request. Just used 2 headers.
            User Agent from a firefox browser and Accept to describe wich format of response
            it's expected to arrive
        """
        headers = {}
        headers['User-Agent'] = userAgent if userAgent else 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
        headers['Accept'] = 'text/*'

        return headers

    def make_request(self, url=None):
        """
            Method to do the request and create a parser instance with this
            response
        """
        self.URL = url if url else self.URL
        if not self.URL:
            return 1
        
        headers = self.construct_headers()
        resp = get(url=self.URL, headers=headers)
        # Especify we want a HTML parse
        parser = BeautifulSoup(resp.text, 'html.parser')

        return parser
    
    def get_full_text(self, url=None):
        """
            Method to get all the text in a web page. It includes tags like
            h1, h2, h3, p, pre, and anothers
        """

        parser = self.make_request(url if url else None)
        return parser.get_text()

  

if __name__ == "__main__":
    p = Html2Text()
    text =p.get_full_text('https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html')
    print(text)
    
