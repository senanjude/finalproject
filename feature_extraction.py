import re
from functools import partial
URL_REGEX = ";|\/|\?|:|@|&|=|\+|$|,|-|\."

TEMPING_WORDS = [“money”,”discount”]


def validate_url(url):
    return url.startswith("http://") or url.startswith("https://")

def url_length(url):
    return len(url)

def get_token(url):
    return list(filter(lambda x:x != None and x != "",re.split(URL_REGEX, url)))

tokens = get_token(url)

def max_token_length(tokens):
    maximum = 0
    for token in tokens:
        if maximum < len(token):
            maximum = len(token)
    return maximum

def get_domain_length(tokens):
    return len(tokens[2])

def count_chars(char,string):
    return len(list(filter(lambda x: x == char,string)))

get_number_dots = partial(count_chars,".")

get_number_qms = partial(count_chars,"?")

get_number_fs = partial(count_chars,"/")

def get_num_digits(url):
    return len(list(filter(lambda char: char.isdigit(),url)))

def get_num_special_chars(url):
    return len(list(filter(lambda char: not char.isalnum(),url)))

def check_exe(url):
    return ".exe" in url

def check_install(url):
    return ".install" in url

def check_com(url):
    return ".com" in url
def check_php(url):
    return ".php" in url

def check_gov(url):
    return ".gov" in url

def check_org(url):
    return ".org" in url

def check_edu(url):
    return ".edu" in url

def check_https(url):
    return "https" in url

def check_htm(url):
    return ".htm" in url

def check_html(url):
    return ".html" in url

def check_net(url):
    return ".net" in url

def check_info(url):
    return ".info" in url

def check_js(url):
    return ".js" in url

def check_temp(url):
    count = 0
    url = url.lower()
    for word in TEMPING_WORDS:
        if word in url:
            count += 1
    return count









import re
from functools import partial
import pandas as pd
import csv 

URL_REGEX = ";|\/|\?|:|@|&|=|\+|$|,|-|\."

def validate_url(url):
	return url.startswith("http://") or url.startswith("https://")

def url_length(url):
  return len(url)

def get_token(url):
  return list(filter(lambda x:x != None and x != "",re.split(URL_REGEX, url)))

def max_token_length(tokens):
  maximum = 0
  for token in tokens:
    if maximum < len(token):
      maximum = len(token)
  return maximum

def get_domain_length(tokens):
  return len(tokens[2])

def count_chars(char,string):
  return len(list(filter(lambda x: x == char,string)))

get_number_dots = partial(count_chars,".")

get_number_qms = partial(count_chars,"?")

get_number_fs = partial(count_chars,"/")

def get_num_digits(url):
  return len(list(filter(lambda char: char.isdigit(),url)))

def get_num_special_chars(url):
  return len(list(filter(lambda char: not char.isalnum(),url)))

def check_exe(url):
  return ".exe" in url

def check_install(url):
  return ".install" in url

def check_com(url):
  return ".com" in url

def check_php(url):
  return ".php" in url

def check_gov(url):
  return ".gov" in url

def check_org(url):
  return ".org" in url

def check_edu(url):
  return ".edu" in url

def check_https(url):
  return "https" in url

def check_htm(url):
  return ".htm" in url

def check_html(url):
  return ".html" in url

def check_net(url):
  return ".net" in url

def check_info(url):
  return ".info" in url

def check_js(url):
  return ".js" in url

