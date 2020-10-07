
def is_odd(x):
    if(x%2==0):
        return False
    else:
        return True


def is_palindrome(word):
    if(word==word[::-1]):
        return True
    else:
        return False


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist
    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    arr = []
    for i in range(len(numlist)):
        if(numlist[i] %2 !=0):
            arr.append(numlist[i])
    return arr


def count_words(text):
    """
    return a dictionary of {word: count} in the text
    words should be split by spaces (and nothing else)
    words should be converted to all lowercase
    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
  
    wordlist = text.split()
    my_dict = {i:wordlist.count(i) for i in wordlist}
    return my_dict

        

if __name__ == "__main__":
    print(is_odd(3))
    print(is_odd(4))
    print(is_palindrome("racecar"))
    print(is_palindrome("green"))
    print(only_odds([1, 2, 3, 4, 5, 6]))
    print(count_words("How much wood would a woodchuck chuck if a woodchuck could chuck wood?"))