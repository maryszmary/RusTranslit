from rus_translit import transliterate


TEST_PAIRS = [
    ('kitten', 'китен'),
    ('treatment', 'тритмент'),
    ('cup', 'кап'),
    ('thank', 'сенк'),
    ('quiz', 'квиз')
]

TEST_NON_LATIN = [
    ('ничего', 'ничего'),
    ('ничего is there', 'ничего из зер')
]


def test_transliterate():
    for eng, rus in TEST_PAIRS:
        assert transliterate(eng) == rus


def test_non_latin():
    for eng, rus in TEST_NON_LATIN:
        assert transliterate(eng) == rus