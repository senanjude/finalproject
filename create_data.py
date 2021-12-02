from feature_extraction import *

import pandas as pd
#xls = pd.ExcelFile('UNB_binary_full.xlsx')
#df = xls.parse('Benign_list_big_final')

df = pd.read_csv("UNB_binary_full.csv",encoding="latin-1")

#df = pd.read_excel('UNB_binary_full.xlsx')
#print(df.head())
length = df.shape[0]
print(length)
#i = 0

col_names = [
    "url",
    "valid",
    "url_length",
    "max_token_length",
    "domain_length",
    "no_of_dots",
    "no_of_qms",
    "no_of_fs",
    "no_of_digits",
    "no_of_specials",
    "has_exe",
    "has_install",
    "has_com",
    "has_php",
    "has_gov",
    "has_org",
    "has_edu",
    "has_https",
    "has_htm",
    "has_html",
    "has_net",
    "has_info",
    "has_js",
    "num_tempting",
    "no_of_tokens",
    "no_of_top_lvl_domains",
    "no_of_schar_domain",
    "no_of_schar_path",
    "no_of_url_paths",
    "no_of_punctuations",
    "no_of_hypen",
    "no_of_eqs",
    "no_of_us",
    "no_of_repetition",
    "len_shortest_token",
    "avg_len_token",
    "len_query",
    "ratio_url_path",
    "has_port",
    "has_shorten",
    "label"
    ]

new_df = []

for i,data in df.iterrows(): #range(length):
        
    try:
        url = data.url
        label = data.Label
        tokens = get_token(url)

        valid = validate_url(url)
        url_len = url_length(url)

        mtl =max_token_length(tokens)
        domain_len = get_domain_length(tokens)

        ndot = get_number_dots(url)
        nqms = get_number_qms(url)
        nfs = get_number_fs(url)
        ndig = get_num_digits(url)
        nsc = get_num_special_chars(url)
        cexe = check_exe(url)
        cins = check_install(url)
        ccom = check_com(url)
        cphp = check_php(url)
        cgov = check_gov(url)
        corg = check_org(url)
        cedu = check_edu(url)
        chttps = check_https(url)
        chtm = check_htm(url)
        chtml = check_html(url)
        cnet = check_net(url)
        cinfo = check_info(url)
        cjs = check_js(url)

        ctemp = check_temp(tokens)
        n_of_tokens = len(tokens)

        get_top_lvl_domain = get_num_top_lvl_domain(url)
        get_schar_domain = get_num_schar_in_domain(url)
        get_schar_path = get_num_schar_in_path(url)
        gnp = get_num_path(url)
        gnsc = get_num_schar(url)
        gnh = get_num_hypen(url)
        gneq = get_num_eq(url)
        gnus = get_num_us(url)
        crep = count_rep(url)
        gmintl = get_min_token_len(tokens)
        gavgtl = get_avg_token_len(tokens)
        glq = get_len_query(url)
        grup = get_ratio_url_to_path(url)
        hpn = has_port_num(url)
        hs = has_shorten(url)

        new_row = [
        url,
        valid, 
        url_len, 
        mtl,
        domain_len,    
        ndot, 
        nqms, 
        nfs, 
        ndig, 
        nsc, 
        cexe, 
        cins, 
        ccom, 
        cphp, 
        cgov, 
        corg, 
        cedu ,
        chttps,
        chtm, 
        chtml, 
        cnet, 
        cinfo,
        cjs,
        ctemp,
        n_of_tokens,
        get_top_lvl_domain, 
        get_schar_domain, 
        get_schar_path ,
        gnp, 
        gnsc ,
        gnh, 
        gneq, 
        gnus, 
        crep, 
        gmintl, 
        gavgtl, 
        glq, 
        grup ,
        hpn, 
        hs,
        label]
        new_df.append(new_row)
        print(i)
    except Exception as e:
        print("Failed at",i,"due to",e)
    

new_dataframe = pd.DataFrame(new_df,columns = col_names)
new_dataframe.to_csv("extracted_values",index=False)