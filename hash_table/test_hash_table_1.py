from hash_table.hash_table_1 import *

# def test_add():
#     hash_table=HashTable()
#     hash_table.add('first hasher',412)
#     assert hash_table.contains('first hasher') == True

# def test_contains():
#     hash_table=HashTable()
#     hash_table.add('first hasher',412)
#     assert hash_table.contains('first hasher') == True

# def test_no_key():
#     hash_table=HashTable()
#     hash_table.add("firas","0101")
#     assert hash_table.contains("ahmad")==False

# def test_in_range():
#     hash_table=HashTable()
#     actual=hash_table.hash("17")
#     assert 0 <= actual < hash_table.size

# def test_collision():
#     hash_table=HashTable()
#     hasher_1=hash_table.hash("firas")
#     hasher_2=hash_table.hash("firas")
#     assert hasher_1 == hasher_2

def test_repeated_word_1():
    stringer = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(stringer)
    expected = 'a'
    assert actual == expected

def test_repeated_word_2():
    stringer = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = repeated_word(stringer)
    expected = "was"
    assert actual == expected



def test_repeated_word_3():
    stringer = "it was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(stringer)
    expected = "it"
    assert actual == expected

def test_no_repeated_word():
    stringer = "My tea's gone cold and I'm wondering why I got out of bed at all"
    actual = repeated_word(stringer)
    expected = None
    assert expected == actual