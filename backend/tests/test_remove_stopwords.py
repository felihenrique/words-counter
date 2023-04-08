from application.modules.words.functions import remove_stopwords, tokenize_text

stopwords = [
    'in', 'his', 'was', 'the', 'but', 'sometimes', 'don\'t', 'out', 'as', 'this', 'had', 'been',
    'for', 'last', 'three', 'and', 'he', 'was', 'just'
]

def test_no_stop_words():
    text = """
        Sleeping in his car was never the plan but sometimes things don't work out as planned.
        This had been his life for the last three months and he was just beginning to get used to it.
        He didn't actually enjoy it, but he had accepted it and come to terms with it.
    """
    tokens = tokenize_text(text)
    filtered_tokens = remove_stopwords(tokens)
    print(filtered_tokens)
    for word in filtered_tokens:
        assert not word in stopwords
