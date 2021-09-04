from hash_table.hash_table_1 import *




def test_add():
    hash_table=HashTable()
    hash_table.add('first hasher',412)
    assert hash_table.contains('first hasher') == True

def test_contains():
    hash_table=HashTable()
    hash_table.add('first hasher',412)
    assert hash_table.contains('first hasher') == True

def test_no_key():
    hash_table=HashTable()
    hash_table.add("firas","0101")
    assert hash_table.contains("ahmad")==False

def test_in_range():
    hash_table=HashTable()
    actual=hash_table.hash("17")
    assert 0 <= actual < hash_table.size

def test_collision():
    hash_table=HashTable()
    hasher_1=hash_table.hash("firas")
    hasher_2=hash_table.hash("firas")
    assert hasher_1 == hasher_2