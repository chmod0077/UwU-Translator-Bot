import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import random as rd
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


# i stole this entire function from stackoverflow because i'm not familiar with the
# tenor api at all so i'll maybe try to do it myself but i'm afraid
# it will look identically so maybe not
def retrieve_gif(search_term, limit, api_key):
    # set the api_key and limit
    # load the user's anonymous ID from cookies or some other disk storage
    # anon_id = <from db/cookies>
    # ELSE - first time user, grab and store their the anonymous ID
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % api_key)
    if r.status_code == 200:
        anon_id = json.loads(r.content)["anon_id"]
        # store in db/cookies for re-use later
    else:
        anon_id = ""
    # our test search
    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %
        (search_term, api_key, limit, anon_id))
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


def retrieve_copypasta(file_name):
    """
    file_name: string of the name of the file with extension
    return: random copypasta from file_name
    """
    current_working_file = str(Path(__file__).parent.resolve())
    with open(current_working_file + "/medias/" + file_name, "r+") as file:
        copypasta_file = file.read()
        return rd.choice(copypasta_file.split("\n\n"))


def retrieve_emoji(file_name):
    """
    file_name: string of the name of the file with extension
    return: random emoji from file_name
    """
    current_working_file = str(Path(__file__).parent.resolve())
    with open(current_working_file + "/medias/" + file_name, "r+") as file:
        emoji_file = file.read()
        return rd.choice(emoji_file.split("\n"))


def retrieve_specific_words(file_name):
    """
    file_name: string of the name of the file with extension
    return: dictionary of specific words from file_name
    """
    current_working_file = str(Path(__file__).parent.resolve())
    with open(current_working_file + "/medias/" + file_name, "r+") as file:
        specific_words_file = file.read().split("\n")
        specific_words_dict = {}
        for elt in specific_words_file:
            specific_words_dict[elt.split(":")[0]] = elt.split(":")[1]
        return specific_words_dict


def retrieve_text(file_name):
    """
    file_name: string of the name of the file with extension
    return: random paragraph from file_name delimited by a line jump and a dot.
    """
    current_working_file = str(Path(__file__).parent.resolve())
    file_path = current_working_file + "/medias/" + file_name # full path basically
    with open(file_path, "r+") as full_text:
        split_text = full_text.read().split(".\n") # paragraph delimiter
        return " ".join((rd.choice(split_text)).split("\n")) + "."
