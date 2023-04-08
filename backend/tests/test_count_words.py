from application.modules.words.functions import count_words

def test_empty_list():
    result = count_words([])
    assert type(result) == dict
    assert len(result.keys()) == 0

def test_list_only_one_word():
    words = ['test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test']
    result = count_words(words)
    assert len(result.keys()) == 1
    assert result.get('test') == 9

def test_general_list():
    words = ['test', 'test', 'word', 'word', 'word', 'general', 'general', 'third', 'third', 'one']
    result = count_words(words)
    assert len(result.keys()) == 5

    assert result.get('test') == 2
    assert result.get('word') == 3
    assert result.get('general') == 2
    assert result.get('third') == 2
    assert result.get('one') == 1