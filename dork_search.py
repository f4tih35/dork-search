from serpapi import GoogleSearch
import json


class dork_search:
    @staticmethod
    def get_result(search_types=None, keywords=None, suffixes=None):
        result = None
        for keyword in keywords:
            for search_type in search_types:
                for suffix in suffixes:
                    query = keyword + " " + search_type.value + " site:" + suffix
                    search = GoogleSearch({"q": query,
                                           "api_key": "38661adf0fcfaaecc6e38b3adeb5edce44902e2eacf8ca118e5f62da6005f550"})
                    result = search.get_dict()
        return json.loads(json.dumps(result))
