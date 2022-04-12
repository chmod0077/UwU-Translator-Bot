import random as rd

def list_permutations(word):
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
def uwu_translation(word):
    """
    word: word of string type
    return: word but with the first 'U' translated to 'UwU' or the first 'u' translated to 'uwu'
    """
    uwu_list = ["UwU", "uwu"]
    if word not in list_permutations(uwu_list[1]):
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
    return word + " what's this?"


# assumes that there is an "o" in the word but doesnt know if its already owo
def owo_translation(word):
    """
    word: word of string type
    return: word but with the first 'O' translated to 'OwO' or the first 'o' translated to 'owo'
    """
    owo_list = ["OwO", "owo"]
    if word not in list_permutations(owo_list[1]):
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
    return word + " what's this?"


def r_translation(word):
    word_characters = [char for char in word]
    for i in range(len(word_characters)):
        if word_characters[i] == "r":
            word_characters[i] = "w"
    return "".join(word_characters)


def l_translation(word):
    word_characters = [char for char in word]
    for i in range(len(word_characters)):
        if word_characters[i] == "l":
            word_characters[i] = "w"
    return "".join(word_characters)


def random_stuttering(word):
    if len(word) >= 5 and rd.randrange(1,6) == 1:
        return word[0] + "-" + word
    return word


def random_suffix(word):
    emoji_list = ["(≧▽≦)", "(ㆁωㆁ*)", "(/◕ヮ◕)/", "('・ω・')", "xD", "x)", "^^", "(^o^)", "*blushes*"]
    if rd.randrange(1,16) == 1:
        return word + " " + rd.choice(emoji_list)
    return word


def text_translation(text):
    """
    text: string that can contain any character
    return: text translated to its uwu and owo form
    """ 
    list_of_words = ["you", "are", "to", "peut etre"] # gonna transform this into a dict
    list_of_words_translated = ["u", "r", "2", "pt"] # gonna get rid of that asap
    translated_text = text.split(" ")
    for word in translated_text:
        if any(elt == word for elt in list_of_words): # for specific words
            translated_text[translated_text.index(word)] = list_of_words_translated[[elt in word for elt in list_of_words].index(True)]

        elif "r" in word or "R" in word:
            translated_text[translated_text.index(word)] = r_translation(word)
        elif "l" in word or "L" in word:
            translated_text[translated_text.index(word)] = l_translation(word)

        # o is before u because there is a way higher chance of 'ou' than 'uo'
        elif "o" in word or "O" in word:
            translated_text[translated_text.index(word)] = owo_translation(word)
        elif "u" in word or "U" in word:
            translated_text[translated_text.index(word)] = uwu_translation(word)
    
    current_word_index = 0
    for word in translated_text:
        translated_text[current_word_index] = random_stuttering(word)
        current_word_index += 1

    current_word_index = 0
    for word in translated_text:
        translated_text[current_word_index] = random_suffix(word)
        current_word_index += 1

    return " ".join(translated_text)
