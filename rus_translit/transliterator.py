from string import ascii_letters
from eng_to_ipa import convert
from .mappings import REGULAR_DICT, VOWEL_EXTRA_DICT, KNOWN_WORDS


ASCII_LETTERS = set(ascii_letters)


def is_ascii(s):
    """
    There is no str.isascii in python 3.6
    """
    return bool(set(s) & ASCII_LETTERS)


def transliterate_word(word):
    if word.lower() in KNOWN_WORDS:
        return KNOWN_WORDS[word.lower()]

    transcription = convert(word).replace('ˈ', '').replace('ˌ', '')
    result = ''

    for i, letter in enumerate(transcription):
        
        if letter == 'æ' and i == 0: 
            result += 'э'
                
        elif letter == 'ɑ' and i == len(transcription)-1:
            result += "а"
        
        elif letter == 'j' and i != len(transcription)-1 and transcription[i+1] in ["u", 'ʊ']: 
            continue
            
        elif letter in 'ɹ' and i==len(transcription)-2 and word.endswith("er"):
            result += "ер"
                
        elif letter in 'ɹr' and i != 0 and transcription[i-1] == "s":
            result += "ер"
            
        elif letter == "ə" and i == 0 and word[0].lower() != "u":
            result += VOWEL_EXTRA_DICT.get(word[0].lower(), "э")

        elif letter == "ə" and word.lower()[i] == "u":
            result += "а"
            
        elif letter == "ə" and transcription.endswith("iə") and i == len(transcription)-1:
            result += "я"
                
        elif letter == "ə" and transcription.endswith("ə") and i == len(transcription)-1:
            result += "а"
            
        elif letter == "w" and i > 0 and transcription[i-1] == "o":
            continue
            
        elif letter == "u" and i!=0 and transcription[i-1] == "j":
            result += "ью"
                
        elif letter == "θ" and i == len(transcription)-1:
            result += "с"

        elif letter == 'ŋ' and i + 1 < len(transcription) and transcription[i + 1] == 'k':
            result += 'н'

        elif letter == 'w' and i > 0 and transcription[i - 1] == 'k':
            result += 'в'
                
        else:
            if letter in REGULAR_DICT:
                result += REGULAR_DICT[letter]
            else:
                result += letter
    return result.replace('*', '')


def transliterate(phrase):
    transliterated = []

    for word in phrase.split():
        if is_ascii(word):
            try:
                transliterated.append(transliterate_word(word))
            except:
                transliterated.append(word)
        else:
            transliterated.append(word)
    return ' '.join(transliterated)


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def transliterate_word_mem(word):
    return transliterate_word(word)


def transliterate_memoized(phrase):
    transliterated = []

    for word in phrase.split():
        if is_ascii(word):
            transliterated.append(transliterate_word_mem(word))
        else:
            transliterated.append(word)
    return ' '.join(transliterated)
