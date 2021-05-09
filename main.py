from dork_search import dork_search
from search_type_enum import search_type

search_types = [search_type.OPEN_FTP_SERVER] # example
keywords = [''] # example
suffixes = ['.gov.br'] # example

result = dork_search.get_result(search_types,keywords,suffixes)

if('error' not in result):
    for value in result['organic_results']:
        print("--------------------------")
        print("title: " + value['title'])
        print("link: " + value['link'])
else:
    print("error")
