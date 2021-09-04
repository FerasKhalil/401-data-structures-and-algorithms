# Hashtables
<!-- Short summary or background information -->
- Hash tables allow the storage and retrieval of data in an average time of O(1). At its most basic level, a hash table data structure is just an array. Data is stored into this array at specific indices designated by a hash function. A hash function is a mapping between the set of input data and a set of integers
- Source from (https://www.sparknotes.com/cs/searching/hashtables/summary/#:~:text=Hash%20tables%20allow%20the%20storage,and%20a%20set%20of%20integers.)
## Challenge
<!-- Description of the challenge -->
- Implement a Hashtable Class with the following methods:
- add, contains, find, hash

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Big O of time is: O(1)
- Big O of space is: O(n)

## API
<!-- Description of each method publicly available in each of your hashtable -->
- add method:
    add a value to the hashtable by its key 
    parameters:
    key: a string
    value: any type
    Arrgument: key and value 
    return: nothing


- find method:
    this function will search in the hashtable about the key and return the value
    parameters:
    key: a string
    return: the value 


- contains method: 
   this function will check if the there is a value for the key 
    parameters:
    key: a string
    return: a boolean
    
