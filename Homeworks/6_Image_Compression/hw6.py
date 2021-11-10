'''
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def count_bit(s, bit):
    if s == "":
        return 0
    if s[0] == bit:
        return 1 + count_bit(s[1:], bit)
    else:
        return 0
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n%2==1:
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n//2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        if s[0] == '1':
            return binaryToNum(s[1:]) + 2**(len(s)-1)
        else:
            return binaryToNum(s[1:])
def pad(s):
    return '0'*(COMPRESSED_BLOCK_SIZE - len(s)) + s
def compress(s):
    if s == '':
        return ''
    else:
        zeros = count_bit(s[:MAX_RUN_LENGTH], '0')
        if s[zeros:] == '':
            return pad(numToBinary(zeros))
        ones = count_bit(s[zeros:zeros + MAX_RUN_LENGTH], '1')
        return pad(numToBinary(zeros)) + pad(numToBinary(ones)) + compress(s[zeros+ones:])
def uncompress(s):
    if s == '':
        return ''
    zeros = binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) * '0'
    ones = binaryToNum(s[COMPRESSED_BLOCK_SIZE:2*COMPRESSED_BLOCK_SIZE]) * '1'
    return zeros + ones + uncompress(s[2*COMPRESSED_BLOCK_SIZE:])
def compression(s):
    return len(compress(s))/len(s)
        
