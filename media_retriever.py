# i stole this entire code from stackoverflow because i'm not familiar with the
# tenor api at all so i'll maybe try to do it myself but i'm afraid
# it will look identically so maybe not

import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import random as rd
import os


def retrieve_gif(search_term, limit):
    # set the apikey and limit
    apikey = os.getenv("api_key")  # test value
    # load the user's anonymous ID from cookies or some other disk storage
    # anon_id = <from db/cookies>
    # ELSE - first time user, grab and store their the anonymous ID
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)
    if r.status_code == 200:
        anon_id = json.loads(r.content)["anon_id"]
        # store in db/cookies for re-use later
    else:
        anon_id = ""
    # our test search
    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %
        (search_term, apikey, limit, anon_id))
    if r.status_code == 200:
        url_list = []
        # load the GIFs using the urls for the smaller GIF sizes
        #pp = pprint.PrettyPrinter(indent=4)
        gif_list = json.loads(r.content)
        # pp.pprint(top_8gifs) #pretty prints the json file.
        for i in range(len(gif_list['results'])):
            # This is the url from json.
            url = gif_list['results'][i]['media'][0]['gif']['url']
            url_list.append(url)
        return rd.choice(url_list)
    else:
        gif_list = None
