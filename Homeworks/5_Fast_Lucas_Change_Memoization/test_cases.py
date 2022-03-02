from hw5 import *
import sys

sys.setrecursionlimit(10000)

class Tests():
    
    def __init__(self):
        self.tests = [
            {
                "func": fast_lucas,
                "possible_points": 40,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": 2,
                        "expected": 3,
                        "points": 8
                    },
                    {
                        "input": 10,
                        "expected": 123,
                        "points": 8
                    },
                    {
                        "input": 20,
                        "expected": 15127,
                        "points": 8
                    },
                    {
                        "input": 30,
                        "expected": 1860498,
                        "points": 8
                    },
                    {
                        "input": 60,
                        "expected": 3461452808002,
                        "points": 8
                    }
                ]
            },
            {
                "func": fast_change,
                "possible_points": 40,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "inputs": [420, [1, 5, 10, 25, 50, 100]],
                        "expected": 6,
                        "points": 8
                    },
                    {
                        "inputs": [337, [1, 5]],
                        "expected": 69,
                        "points": 8
                    },
                    {
                        "inputs": [12345, [5, 10, 100, 1000, 10000]],
                        "expected": 11,
                        "points": 8
                    },
                    {
                        "inputs": [1, [1]],
                        "expected": 1,
                        "points": 8
                    },
                    {
                        "inputs": [30, [1, 5, 10, 25, 50, 100]],
                        "expected": 2,
                        "points": 8
                    }
                ]
            }
        ]
