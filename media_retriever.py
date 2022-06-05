import requests
import json
import urllib.request
import urllib.parse
import urllib.error
import random as rd

# i stole this entire function from stackoverflow because i'm not familiar with the
# tenor api at all so i'll maybe try to do it myself but i'm afraid
# it will look identical so maybe not


class MediaRetriever:
    def __init__(self, current_dir: str) -> None:
        self.current_dir = current_dir

    def retrieve_gif(self, search_term: str, search_limit: int, api_key: str) -> str:
        """
        requests search_limit gifs to the tenor api and sends one of them
            search_term: what gif to search for in the search bar
            search_limit: number of gifs to search for
            api_key: your tenor api key
        returns: random gif url from your gif list
        """
        r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % api_key)
        if r.status_code == 200:
            anon_id = json.loads(r.content)["anon_id"]
        else:
            anon_id = ""
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" %
            (search_term, api_key, search_limit, anon_id))
        if r.status_code == 200:
            url_list = []
            gif_list = json.loads(r.content)
            for i in range(len(gif_list['results'])):
                # This is the url from json.
                url = gif_list['results'][i]['media'][0]['gif']['url']
                url_list.append(url)
            return rd.choice(url_list)
        else:
            gif_list = None

    def retrieve_copypasta(self, file_name: str) -> str:
        """
        retrieves a random copypasta from your copypasta file
            file_name: name of the file with extension
        return: random copypasta from file_name
        """
        with open(self.current_dir + file_name, "r+") as file:
            copypasta_file = file.read()
            return rd.choice(copypasta_file.split("\n\n"))

    def retrieve_emoji(self, file_name: str) -> str:
        """
        retrieves a random emoji from your emoji file
            file_name: name of the file with extension
        return: random emoji from file_name
        """
        with open(self.current_dir + file_name, "r+") as file:
            emoji_file = file.read()
            return rd.choice(emoji_file.split("\n"))

    def retrieve_specific_words(self, file_name: str) -> str:
        """
        retrieves a random copypasta from your copypasta file
            file_name: name of the file with extension
        return: random copypasta from file_name
        """
        with open(self.current_dir + file_name, "r+") as file:
            specific_words_file = file.read().split("\n")
            specific_words_dict = {}
            for elt in specific_words_file:
                specific_words_dict[elt.split(":")[0]] = elt.split(":")[1]
            return specific_words_dict

    def retrieve_text(self, file_name: str) -> str:
        """
        retrieves a random paragraph from your text file
            file_name: name of the file with extension
        return: random paragraph from file_name delimited by a line jump and a dot
        """
        file_path = self.current_dir + file_name  # full path basically
        with open(file_path, "r+") as full_text:
            split_text = full_text.read().split(".\n")  # paragraph delimiter
            return " ".join((rd.choice(split_text)).split("\n")) + "."
