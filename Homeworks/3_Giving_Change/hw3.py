def giveChange(amount, coins):
    '''Assuming amount is a non-negative integer and coins is a list 
    of coin values, it returns the minimum amount of coins to 
    make up the amount and the list of coins in that optimal solution'''
    if amount <= 0:
        return [0, []]
    elif coins == []:
        return [float("inf"), []]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        use = giveChange(amount - coins[0], coins[0:])
        lose = giveChange(amount, coins[1:])
        if use[0] < lose[0]:
            return [use[0] + 1, use[1] + [coins[0]]]
        else:
            return lose

def testChange():
    assert giveChange(48, [1, 5, 10, 25, 50]) == [6, [25, 10, 10, 1, 1, 1]]
    assert giveChange(48, [1, 7, 24, 42]) == [2, [24, 24]]
    assert giveChange(35, [1, 3, 16, 30, 50]) == [3, [16, 16, 3]]

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(e, L):
    """Assuming e is a single letter string and L is a list that
    associates wach letter of the alphabet with a Scrabble score, letterScore
    returns the score of the letter according to L."""
    if L == []:
        return []
    elif L[0][0] == e:
        return L[0][1]
    else:
        return letterScore(e, L[1:])

def wordScore(e, L):
    """Assuming e is a string and L is a list associating each letter with a
    scrabble score, returns the sum of each letter in S and thus the score of the word"""
    if L == [] or e == "":
        return 0
    return letterScore(e[0], L) + wordScore(e[1:], L)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return list(map(lambda word: [word, wordScore(word, scores)], dct)) 

def testScore():
    assert wordsWithScore(['a', 'am', 'at', 'apple'], scrabbleScores) == [['a', 1], ['am', 4], ['at', 2], ['apple', 9]]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    if n == 0 or L == []:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])

def testTake():
    assert take(2, [1, 2, 3, 4, 5]) == [1, 2]
    assert take(0, range(0,3)) == []
    assert take(3, [1, 2]) == [1, 2]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return L
    else:
        return drop(n-1, L[1:])

def testDrop():
    assert drop(2, range(0,5)) == [2,3,4]
    assert drop(0, range(0,8)) == range(0,8)
    assert drop(5, range(0,4)) == []

