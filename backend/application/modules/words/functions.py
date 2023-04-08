from spacy.lang.en import English
from string import punctuation
from typing import List

ext_punctuation = punctuation + '\n' + '\r'

nlp = English()

def tokenize_text(text: str):
    """
        Takes a text and turn it into individual words. 
        It removes special characters and turns words into lowercase
    """
    tokens_info = nlp(text)
    # here we use token[0] to take only the first character 
    # from special characters clusters like ... and >=
    tokens = [token.text.lower() for token in tokens_info if not token.text[0] in ext_punctuation]
    return tokens

def remove_stopwords(words: List[str]) -> List[str]:
    """
        Takes a list of words and filter the list to remove the stopwords.
        Stopwords are words that usually doesn't have relevance when doing text analysis,
        like connectives
    """
    filtered_list = [word for word in words if word.lower() not in nlp.Defaults.stop_words]
    return filtered_list

def count_words(words: List[str]):
    """
        Takes a list of words, counts the ocurrences of every word
        and turns into a dictionary where the key is the word and the value is the number
        of ocurrences 
    """
    word_dict = {}
    for word in words:
        word_dict[word] = (word_dict.get(word) or 0) + 1
    return word_dict