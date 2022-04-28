import re
from functools import partial
from urllib.parse import urlparse
import numpy as np 
URL_REGEX = ";|\/|\?|:|@|&|=|\+|$|,|-|\."
file_shorten = open('tinyurl.txt','r')


def validate_url(url):
    return url.startswith("http://") or url.startswith("https://")

def url_length(url):
    return len(url)

def get_token(url):
    return list(filter(lambda x:x != None and x != "",re.split(URL_REGEX, url)))

#tokens = get_token(url)

def get_domain_length(url):
    o = urlparse(url)
    hostname = o.hostname
    if hostname is None or hostname == "":
          return 0
    d = hostname.split(".")
    if d[0] == "www":
          domain = d[1]
    elif d[0].isnumeric():
          domain = ""
    else:
          domain = d[0]
    return len(domain)

def count_chars(char,string):
    return len(list(filter(lambda x: x == char,string)))

get_number_fs = partial(count_chars,"/")

def get_num_special_chars(url):
    return len(list(filter(lambda char: not char.isalnum(),url)))

def check_php(url):
    return ".php" in url

def check_https(url):
    return "https" in url

def check_htm(url):
    return ".htm" in url

def check_html(url):
    return ".html" in url

def check_net(url):
    return ".net" in url

def get_num_schar_in_domain(url):
      domain = list(filter(lambda x:x != "" and x != None,url.split("/")))[1]
      return len(list(filter(lambda x:x == "-",domain)))

def get_num_schar_in_path(url):
      path = "".join(list(filter(lambda x:x != "" and x != None,url.split("/")))[2:])
      count = 0 
      for char in path:
            if not char.isalnum():
                  count += 1
      return count

def get_num_path(url):
      o = urlparse(url)
      path = list(filter(lambda x: x!= None and x != "",o.path.split("/")))
      return len(path)

def get_num_schar(url):
  return len(list(filter(lambda x:not x.isalnum(),url)))

def get_num_hypen(url):
  return len(list(filter(lambda x:x == "-",url)))

def count_rep(url):
  count = dict()
  total = 0
  for elem in url:
    count[elem] = count.get(elem,0) + 1
  for elem in count:
    if count[elem] > 1:
      total += 1 
  return total

def get_min_token_len(tokens):
  return min(map(lambda x:len(x),tokens))

def get_avg_token_len(tokens):
  length = len(tokens)
  total = sum(map(lambda x:len(x),tokens))
  return total/length 

def has_shorten(url):
  for line in file_shorten.readlines():
    if line[:-1] in url:
      return True
  return False

def get_ratio_vowel_consonant(url):
      alphabets = list(filter(lambda x:x.isalpha(),url))
      valid_vowels = ["a","e","i","o","u"]
      count_vowels = 0
      for c in alphabets:
            if c in valid_vowels:
                  count_vowels += 1
      try:
        ratio = count_vowels/(len(alphabets) - count_vowels)
        return ratio
      except Exception as e:
        return 0
      
def get_std_token_len(tokens):
     lengths = list(map(len,tokens))
     return np.std(lengths) 