import whois
import dns.resolver
import datetime
import requests
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

#input assumes that url starts with http:// or https://
def get_num_top_lvl_domain(url):
      domain = list(filter(lambda x:x != "" and x != None,url.split("/")))[1]
      with open(DOMAIN_FILE) as file:
        valid_domains = file.readlines()
        valid_domains = [line.rstrip() for line in valid_domains]
      for valid_domain in valid_domains:
            if domain.endswith("."+valid_domain):
                  return len(valid_domain.split("."))
	
#schar = special character in domain
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

#re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url) to find domain from url
def get_num_path(url):
      o = urlparse(url)
      path = list(filter(lambda x: x!= None and x != "",o.path.split("/")))
      return len(path)

#number of special characters in url
def get_num_schar(url):
  return len(list(filter(lambda x:not x.isalnum(),url)))

def get_num_hypen(url):
  return len(list(filter(lambda x:x == "-",url)))

def get_num_eq(url):
  return len(list(filter(lambda x:x == "=",url)))

def get_num_us(url):
  return len(list(filter(lambda x:x == "_",url)))

#counts number of characters with more than 1 count
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

def get_len_query(url):
  o = urlparse(url)
  query = o.query 
  return len(query)

def get_ratio_url_to_path(url):
  o = urlparse(url)
  path = o.path
  return len(url) / len(path)

def has_shorten(url):
  f = open('tinyurl.txt','r')
  for line in f.readlines():
    if line[:-1] in url:
      return True
  return False

def domain_reg_length(url):
  data = whois.whois(url)
  c_date = data['creation_date']
  e_date = data['expiration_date']
  return (e_date-c_date).days/365

def has_dns_record(url):
  try:
    data = dns.resolver.resolve(url)
    return True
  except Exception as e:
    return False

def age_of_domain(url):
  data = whois.whois(url)
  c_date = data['creation_date']
  return (datetime.datetime.now()-c_date).days/365

def has_redirection(url):
  try:
    responses = requests.get(url)
    if len(responses.history) >= 1:
      return True
    else:
      return False
  except:
    return False

def has_port_num(url):
  part = url.split('/')[2]
  if ':' in part:
    port = part.split(':')[1]
    if 0 <= int(port) <= 65535:
      return True
    else:
      return False
  else:
    return False

