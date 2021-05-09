from serpapi import GoogleSearch
import json
import os


class dork_search:
    @staticmethod
    def get_result(search_types=None, keywords=None, suffixes=None):
        result = None
        for keyword in keywords:
            for search_type in search_types:
                for suffix in suffixes:
                    query = keyword + " " + search_type.value + " site:" + suffix
                    search = GoogleSearch({"q": query,
                                           "api_key": os.environ.get('API_KEY')})
                    result = search.get_dict()
        return json.loads(json.dumps(result))
