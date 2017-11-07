import urllib.request
import os
import re
import time
import socket
from bs4 import BeautifulSoup

def crawerEach(url, urldir):
	resp = urllib.request.urlopen(url)
	html = resp.read().decode('gbk')
	soup = BeautifulSoup(html)
	items = soup.find('body').find('div', id='main').find(name='div', attrs={'class':'t','style':})