from feature_extraction import *
import pandas as pd
import pickle

randf_model = pickle.load(open('models/randf_model.pickle', 'rb'))

col_names = [
    "has_php",
    "has_htm",
    "has_html",
    "has_net",
    "has_shorten",
    "url_length",
    "domain_length",
    "no_of_fs",
    "no_of_specials",
    "no_of_schar_domain",
    "no_of_schar_path",
    "no_of_url_paths",
    "no_of_punctuations",
    "no_of_hypen",
    "no_of_repetition",
    "len_shortest_token",
    "avg_len_token",
    "ratio_vowel_consonant",
    "std_token_len",
    ]

def extract(url):  
  df = []
  tokens = get_token(url)

  cphp = 1 if check_php(url) else 0
  chtm = 1 if check_htm(url) else 0
  chtml = 1 if check_html(url) else 0
  cnet = 1 if check_net(url) else 0
  hs = 1 if has_shorten(url) else 0
  url_len = url_length(url)
  domain_len = get_domain_length(url)
  nfs = get_number_fs(url)
  nsc = get_num_special_chars(url)
  get_schar_domain = get_num_schar_in_domain(url)
  get_schar_path = get_num_schar_in_path(url)
  gnp = get_num_path(url)
  gnsc = get_num_schar(url)
  gnh = get_num_hypen(url)
  crep = count_rep(url)
  gmintl = get_min_token_len(tokens)
  gavgtl = get_avg_token_len(tokens)
  rvc = get_ratio_vowel_consonant(url)
  stl = get_std_token_len(tokens)

  new_row = [cphp, chtm, chtml, cnet, hs, url_len, domain_len, nfs, nsc, get_schar_domain,
             get_schar_path, gnp, gnsc, gnh, crep, gmintl, gavgtl, rvc, stl]
  df.append(new_row)

  return pd.DataFrame(df, columns=col_names)

def test(url):
  df = extract(url)
  out = randf_model.predict(df)

  return out

if __name__ == "__main__":
  test_data = pd.read_csv("test_dataset2.csv")
  total = len(test_data)
  out = 0

  for i, data in test_data.iterrows():
    url = data.url
    # if url.startswith('"'):
    #   url = url[1:-1]
    # if not url.startswith("http"):
    #   total -= 1
    #   print("*")
    url = "https://www."+url
    if test(url) == 'benign':
      out +=1
    else:
      print(i, url)
  print(out, total, out/total)