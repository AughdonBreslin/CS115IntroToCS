from hw8 import *
import sys
from unittest import *

class Tests():
    
    def __init__(self):

        sequence = [
            '0' * 64,
            '01' * 32,
            '10' * 32,
            '0' * 31 + '1' * 31 + '00',
            '0' * 32 + '1' * 32
        ]

        self.tests = [
            {
                "func": listOfRunLengths,
                "possible_points": 40,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": sequence[0],
                        "expected": [64],
                        "points": 8
                    },
                    {
                        "input": sequence[1],
                        "expected": [1]*64,
                        "points": 8
                    },
                    {
                        "input": sequence[2],
                        "expected": [1]*64,
                        "points": 8
                    },
                    {
                        "input": sequence[3],
                        "expected": [31, 31, 2],
                        "points": 8
                    },
                    {
                        "input": sequence[4],
                        "expected": [32, 32],
                        "points": 8
                    }
                ]
            },
            {
                "func": findRunBits,
                "possible_points": 40,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": sequence[0],
                        "expected": 7,
                        "points": 8
                    },
                    {
                        "input": sequence[1],
                        "expected": 1,
                        "points": 8
                    },
                    {
                        "input": sequence[2],
                        "expected": 1,
                        "points": 8
                    },
                    {
                        "input": sequence[3],
                        "expected": 6,
                        "points": 8
                    },
                    {
                        "input": sequence[4],
                        "expected": 6,
                        "points": 8
                    }
                ]
            }
        ]