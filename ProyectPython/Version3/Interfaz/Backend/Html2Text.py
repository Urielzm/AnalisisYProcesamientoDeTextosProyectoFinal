from requests import get, head
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from re import search, compile, escape, IGNORECASE

class Html2Text(object):
    def __init__(self, url=None):
        """
            Class constructor. Just needed URL to work. It's not necessary
            to create an instance of this class
        """
        self.URL = url
        self.response = ''

    def set_url(self, url):
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

    def make_request(self):
        """
            Method to do the request and create a parser instance with this
            response
        """
        
        headers = self.construct_headers()
        self.response = get(url=self.URL, headers=headers).text

    def html_to_text(self, filtered_response):
        """
            Method to get all the text in a web page. It includes tags like
            h1, h2, h3, p, pre, and anothers
        """
        parser = BeautifulSoup(filtered_response, 'html.parser')
        return parser.get_text()


    def try_connection(self):
        try:
            head(self.URL, headers=self.construct_headers())
            return True

        except ConnectionError:
            return False

    def deconstruct_response(self, resp):
        return resp.split('\n')

    def filtered_response(self):
        #to_delete = ['href']
        
        response_list = self.deconstruct_response(self.response)

        response = ''
        regex = self.create_a_tags_regex()
        regex = compile(regex)

        for line in response_list:
            find = search(regex, line)
            if not find:
                response += line + '\n'
            else:
                response += line.replace(find.group(0), '')

        #print(response)
        return response
  
    def remove_blank_spaces(self, text):
        text_list = self.deconstruct_response(text)
        
        clear_text = ''
        for line in text_list:
            if line != '':
                clear_text += line + '\n'

        return clear_text

    def get_text(self, url):
        self.set_url(url)
        if not self.try_connection():
            return None

        self.make_request()
        filtered_response = self.filtered_response()
        text = self.html_to_text(filtered_response)
        return self.remove_blank_spaces(text)

    def get_a_tags(self):
        parser = BeautifulSoup(self.response, 'html.parser')
        tag_list = parser.find_all('a')
        for i in range(len(tag_list)):
            tag_list[i] = str(tag_list[i])

        return tag_list

    def create_a_tags_regex(self):
        tag_list = self.get_a_tags()
        regex = '('
        for element_tag in tag_list:
            regex += element_tag + '|'
        return regex[:-1] + ')'

if __name__ == "__main__":
    p = Html2Text()
    #print(p.get_a_tags())
    text = p.get_text('https://esasasa.wikipedia.org/wiki/Resumen')
    print(text)
    
