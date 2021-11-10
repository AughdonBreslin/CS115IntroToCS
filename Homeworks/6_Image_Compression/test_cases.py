from hw6 import *
import sys
from unittest import *

class Tests():
    
    def __init__(self):

        sequence = [
            '0' * 64,
            '01' * 32,
            '10' * 32,
            '0' * MAX_RUN_LENGTH + '1' * MAX_RUN_LENGTH + '0' * (64 - 2 * MAX_RUN_LENGTH),
            '0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2)
        ]

        self.tests = [
            {
                "func": compression,
                "possible_points": 25,
                "cmp": lambda x, y: round(x,2) == round(y,2),
                "tests": [
                    {
                        "input": sequence[0],
                        "expected": 0.39,
                        "points": 5
                    },
                    {
                        "input": sequence[1],
                        "expected": 5.0,
                        "points": 5
                    },
                    {
                        "input": sequence[2],
                        "expected": 5.08,
                        "points": 5
                    },
                    {
                        "input": sequence[3],
                        "expected": 0.23,
                        "points": 5
                    },
                    {
                        "input": sequence[4],
                        "expected": 0.47,
                        "points": 5
                    }
                ]
            },
            {
                "func": uncompress,
                "possible_points": 25,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": compress(sequence[0]),
                        "expected": sequence[0],
                        "points": 5
                    },
                    {
                        "input": compress(sequence[1]),
                        "expected": sequence[1],
                        "points": 5
                    },
                    {
                        "input": compress(sequence[2]),
                        "expected": sequence[2],
                        "points": 5
                    },
                    {
                        "input": compress(sequence[3]),
                        "expected": sequence[3],
                        "points": 5
                    },
                    {
                        "input": compress(sequence[4]),
                        "expected": sequence[4],
                        "points": 5
                    }
                ]
            },
            {
                "func": compress,
                "possible_points": 25,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": sequence[0],
                        "expected": '1111100000111110000000010',
                        "points": 5
                    },
                    {
                        "input": sequence[1],
                        "expected": '00001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001',
                        "points": 5
                    },
                    {
                        "input": sequence[2],
                        "expected": '0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001',
                        "points": 5
                    },
                    {
                        "input": sequence[3],
                        "expected": '111111111100010',
                        "points": 5
                    },
                    {
                        "input": sequence[4],
                        "expected": '111110000000001111110000000001',
                        "points": 5
                    }
                ]
            }
        ]
