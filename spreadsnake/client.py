import httplib
from bs4 import BeautifulSoup

HOST = "api.spreadshirt.com"


class Client(object):

    """docstring for Client"""

    def articles(self, shop_id):
        return self.get(fragment="shops/{}/articles".format(shop_id))

    def get(self, fragment):
        conn = httplib.HTTPConnection(HOST)
        path = "/api/v1/{}".format(fragment)
        conn.request("GET", path)
        response = conn.getresponse()
        return [response.status, response.read()]
