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


def text_translation(text):
    """
    text: string that can contain any character
    return: text translated to its uwu and owo form
    """
    translated_text = []
    for word in text.split(" "):
        # o is before u because there is a way higher chance of 'ou' than 'uo'
        # in english
        if "o" in word or "O" in word:
            translated_text.append(owo_translation(word) + " ")
        elif "u" in word or "U" in word:
            translated_text.append(uwu_translation(word) + " ")
        else:
            translated_text.append(word + " ")
    return "".join(translated_text)
