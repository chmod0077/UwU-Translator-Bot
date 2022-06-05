# i'm gonna try to shorten this code as much as possible
# but for now i'll just leave it as is

import random as rd
from media_retriever import MediaRetriever
from pathlib import Path


class TextTranslator:
    def __init__(self) -> None:
        current_dir = str(Path(__file__).parent.resolve()) + '/medias/'
        self.MR = MediaRetriever(current_dir)

    def list_permutations(self, word):
        """
        word: word of string type
        return: every possible (i guess) way to uppercase and lowercase a word, the name "permutation" is wrongly used
        """
        permutations = [word.lower(), word.upper()]
        for i in range(len([char for char in word])):
            # capitalizes the i character
            new_word = [char for char in word]
            new_word[i] = new_word[i].upper()
            permutations.append("".join(new_word))
            # capitalizes the other characters except i
            new_word = [char.upper() for char in word]
            new_word[i] = new_word[i].lower()
            permutations.append("".join(new_word))
        return permutations

    # assumes that there is an "o" in the word but doesnt know if its already uwu

    def uwu_translation(self, word):
        """
        word: word of string type
        return: word but with the first 'U' translated to 'UwU' or the first 'u' translated to 'uwu'
        """
        uwu_list = ["UwU", "uwu"]
        if word.replace(".", "") not in self.list_permutations(uwu_list[1]):
            word_characters = [char for char in word]
            if uwu_list[0][0] in word_characters:
                # I voluntarily don't want to have more than one UwU per word
                U_index = word_characters.index(uwu_list[0][0])
                word_characters[U_index] = uwu_list[0]
            else:
                # I also voluntarily don't want to have more than one uwu per word
                u_index = word_characters.index(uwu_list[1][0])
                word_characters[u_index] = uwu_list[1]
            return "".join(word_characters)
        return word

    # assumes that there is an "o" in the word but doesnt know if its already owo

    def owo_translation(self, word):
        """
        word: word of string type
        return: word but with the first 'O' translated to 'OwO' or the first 'o' translated to 'owo'
        """
        owo_list = ["OwO", "owo"]
        if word.replace(".", "") not in self.list_permutations(owo_list[1]):
            word_characters = [char for char in word]
            if owo_list[0][0] in word_characters:
                # I voluntarily don't want to have more than one OwO per word
                O_index = word_characters.index(owo_list[0][0])
                word_characters[O_index] = owo_list[0]
            else:
                # I also voluntarily don't want to have more than one owo per word
                o_index = word_characters.index(owo_list[1][0])
                word_characters[o_index] = owo_list[1]
            return "".join(word_characters)
        return word

    def r_translation(self, word):
        """
        word: word of string type
        return: word but with every 'r' translated to 'w'
        """
        word_characters = [char for char in word]
        for i in range(len(word_characters)):
            if word_characters[i] == "r":
                word_characters[i] = "w"
        return "".join(word_characters)

    def l_translation(self, word):
        """
        word: word of string type
        return: word but with every 'l' translated to 'w'
        """
        word_characters = [char for char in word]
        for i in range(len(word_characters)):
            if word_characters[i] == "l":
                word_characters[i] = "w"
        return "".join(word_characters)

    def random_stuttering(self, word):
        """
        word: word of string type
        return: word with a stuttering effect according to a certain probability, else, word
        """
        if len(word) >= 5 and rd.randrange(1, 6) == 1:
            return word[0] + "-" + word
        return word

    def random_suffix(self, word):
        """
        word: word of string type
        return: word with a suffix according to a certain probability, else, word
        """
        if rd.randrange(1, 16) == 1:
            return word + " " + self.MR.retrieve_emoji("emojis.txt")
        return word

    def text_translation(self, text):
        """
        text: string that can contain any character
        return: text translated to its uwu and owo form
        """
        translated_text = text.split(" ")
        for word in translated_text:
            specific_words_dict = self.MR.retrieve_specific_words(
                "specific_words.txt")
            if any(key == word for key in specific_words_dict.keys()
                   ):  # for specific words
                # word that is in both specific_words_dict and text
                confirmed_word = [
                    key for key in specific_words_dict.keys() if key in word][0]
                # replace word in text by its translation in specific_words_dict
                translated_text[translated_text.index(
                    word)] = specific_words_dict[confirmed_word]

            elif "r" in word or "R" in word:
                translated_text[translated_text.index(
                    word)] = self.r_translation(word)
            elif "l" in word or "L" in word:
                translated_text[translated_text.index(
                    word)] = self.l_translation(word)

            # o is before u because there is a way higher chance of 'ou' than 'uo'
            elif "o" in word or "O" in word:
                translated_text[translated_text.index(
                    word)] = self.owo_translation(word)
            elif "u" in word or "U" in word:
                translated_text[translated_text.index(
                    word)] = self.uwu_translation(word)

        # i hate how this looks because it's so poorly made, i apologize for that
        current_word_index = 0
        for word in translated_text:
            translated_text[current_word_index] = self.random_stuttering(word)
            current_word_index += 1

        current_word_index = 0  # same thing, cover your eyes
        for word in translated_text:
            translated_text[current_word_index] = self.random_suffix(word)
            current_word_index += 1

        return " ".join(translated_text)
