import os
import config
from serpapi import GoogleSearch
import json

api_key = config.API_KEY


class dork_search:
    @staticmethod
    def get_result(search_type=None, keywords=None, suffix=None):
        query = ' '.join(keywords) + " " + search_type + " site:" + suffix
        search = GoogleSearch({"q": query, "api_key": os.environ.get(api_key)})
        result = search.get_dict()
        return json.loads(json.dumps(result))
