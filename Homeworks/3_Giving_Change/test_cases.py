from hw3 import *

class Tests():
    
    def __init__(self):
        self.tests = [
            {
                "func": giveChange,
                "possible_points": 15,
                "cmp": lambda x, y: x[0] == y[0] and set(x[1]) == set(y[1]),
                "tests": [
                    {
                        # "inputs" means that they are separate
                        # "input" (singular) means interpret a list as a single input 
                        "inputs": [400, [1, 9, 50, 392]],
                        "expected": [8, [50, 50, 50, 50, 50, 50, 50, 50]],
                        "points": 3 
                    },
                    {
                        "inputs": [32, [1, 5, 10, 25]],
                        "expected": [4, [1, 1, 5, 25]],
                        "points": 3 
                    },
                    {
                        "inputs": [32, [1, 7, 24, 42]],
                        "expected": [3, [1, 7, 24]],
                        "points": 3
                    },
                    {
                        "inputs": [48, [1, 5, 10, 25, 50]],
                        "expected": [6, [25, 10, 10, 1, 1, 1]],
                        "points": 3
                    },
                    {
                        "inputs": [48, [50, 25, 10, 5, 1]],
                        "expected": [6, [25, 10, 10, 1, 1, 1]],
                        "points": 3 
                    }
                ]
            },
            {
                "func": wordsWithScore,
                "possible_points": 15,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [Dictionary, scrabbleScores],
                        "expected": [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]],
                        "points": 5
                    },
                    {
                        "inputs": [Dictionary, list(map(lambda x: [x[0], x[1]*2 + 1], scrabbleScores))],
                        "expected": [['a', 3], ['am', 10], ['at', 6], ['apple', 23], ['bat', 13], ['bar', 13], ['babble', 30], ['can', 13], ['foo', 15], ['spam', 20], ['spammy', 36], ['zzyzva', 84]],
                        "points": 5
                    },
                    {
                        "inputs": [["cats", "are", "cool"], scrabbleScores],
                        "expected": [['cats', 6], ['are', 3], ['cool', 6]],
                        "points": 5
                    }
                ]
            },
            {
                "func": take,
                "possible_points": 20,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [10, ["hello"]],
                        "expected": ["hello"],
                        "points": 5
                    },
                    {
                        "inputs": [3, [1, 2, 3, 4, 5]],
                        "expected": [1, 2, 3],
                        "points": 5
                    },
                    {
                        "inputs": [0, [52, 34]],
                        "expected": [],
                        "points": 5
                    },
                    {
                        "inputs": [1, ["a", "b", "c"]],
                        "expected": ["a"],
                        "points": 5
                    }
                ]
            },
            {
                "func": drop,
                "possible_points": 20,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [10, ["hello"]],
                        "expected": [],
                        "points": 5
                    },
                    {
                        "inputs": [4, [1, 2, 3, 4, 5]],
                        "expected": [5],
                        "points": 5
                    },
                    {
                        "inputs": [0, ["a", "b", "c", "d"]],
                        "expected": ["a", "b", "c", "d"],
                        "points": 5
                    },
                    {
                        "inputs": [1, ["a", "b", "c"]],
                        "expected": ["b", "c"],
                        "points": 5
                    }
                ]
            }

        ]
