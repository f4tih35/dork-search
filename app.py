from dork_search import dork_search
from search_type_enum import type
import sys

index,i1,i2,i3 = 0,0,0,0

for arg in sys.argv:
    if arg == '-k':
        i1 = index
    if arg == '-s':
        i2 = index
    if arg == '-t':
        i3 = index
    index += 1

keywords = sys.argv[i1+1:i2]
suffix = ''.join(sys.argv[i2+1:i2+2])
search_type = type[''.join(sys.argv[i3+1:i3+2])].value

result = dork_search.get_result(search_type,keywords,suffix)

if 'error' not in result:
    for value in result['organic_results']:
        print("--------------------------")
        print("title: " + value['title'])
        print("link: " + value['link'])
else:
    print("error")
