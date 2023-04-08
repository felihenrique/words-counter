from application.modules.words.functions import count_words, remove_stopwords, tokenize_text

def process_text(text: str):
    tokens = tokenize_text(text)
    filtered_tokens = remove_stopwords(tokens)
    return count_words(filtered_tokens)