from repeated_word_1.repeated_word import *


def test_repeated_word():
    stringer = "in this string the repeated word is: repeated . why? because I said so."
    actual = repeated_word(stringer)
    expected = 'repeated'
    assert actual == expected


def test_no_repeated_word():
    stringer = "My tea's gone cold and I'm wondering why I got out of bed at all"
    actual = repeated_word(stringer)
    expected = None
    assert expected == actual