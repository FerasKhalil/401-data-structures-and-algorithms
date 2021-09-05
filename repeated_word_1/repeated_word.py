from collections import Counter 
def repeated_word(user_input)->str: 
    splitter = user_input.split(' ') 
    dict = Counter(splitter)  
    for word in splitter: 
        if dict[word]>1: 
            return word

if __name__ == "__main__":
    stringer = "Believe it or not, in this string the output should be the word: this ,  because it's the first repeated word."            
    print(repeated_word(stringer))