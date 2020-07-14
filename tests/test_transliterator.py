from rus_translit import transliterate


TEST_PAIRS = [
    ('kitten', 'китен'),
    ('treatment', 'тритмент'),
    ('cup', 'кап'),
    ('thank', 'сенк')
]

def test_transliterate():
    for eng, rus in TEST_PAIRS:
        assert transliterate(eng) == rus