# Merge Sort
## [Link to readme](README.md)

## Problem Domain:
You need to write a function that takes in a list and sorts its elements in an ascending order

## Visual: 
Input: [8, 4, 23, 42, 16, 15]
Output: [4, 8, 15, 16, 23, 42]


## Algorithm
* create a function that takes a lisit parameter.
* assign n to equal the length of the list
* always make sure that the n is greater than 1
* assign mid to be half of the n
* left to equal the first half of the list
* right to equal the second half of the list
* call merge_sort function for left and right
* call and create another function that will merge the 2 lists. and give it parameters left, right and the list.
* inside the merge function declare three variables i,j,k to equal 0. 
* make a loop that stops when i is lesss the left length and when j is less than the second length of the list.
* inside loop make sure to assign the values in an ascending order. 
* keep checking until there is no values or elements left out.       

## psuedo code
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left



## Code 
def merge_sort(list):
    n = len(list)
    if n > 1:
        mid = n // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left,right,list)

def merge(left, right, list):
    i=0
    j=0
    k=0
    while i < len(left) and j<len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i+=1
        else:
            list[k] = right[j]
            j+=1
        k+=1
    if i==len(left):
        for element in right[j:]:
            list[k]=element
            k+=1
    else:
        for element in left[i:]:
            list[k]=element
            k+=1

## Big O 
time=O(nLogn)
space=O(n)

## Code Tests      

def test_merge_sort():
    lister = [8, 4, 23, 42, 16, 15]
    merge_sort(lister)
    actual = lister
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

## Verification
1. verify code matches algorithm
2. verify big O
3. test the code to make sure it gives right output    