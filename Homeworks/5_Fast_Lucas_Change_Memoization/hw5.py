'''
Homework 5
'''

lucas_dic = {0:2, 1: 1}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    ##Same as fibonnacci, just the base cases change
    if n in lucas_dic:return lucas_dic[n]
    ans1 = fast_lucas(n - 1)
    lucas_dic[n-1]= ans1
    ans2 = fast_lucas(n - 2)
    lucas_dic[n-2]= ans2
    lucas_dic[n] = ans1 + ans2
    return ans1 + ans2
change_memo = {}
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if (amount, tuple(coins)) in change_memo:
        return change_memo[(amount, tuple(coins))]
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        temp = fast_change(amount, coins[1:])
        return temp
    else:
        use = 1 + fast_change(amount - coins[0], coins)
        lose = fast_change(amount, coins[1:])
        change_memo[(amount, tuple(coins))] = min(use, lose)
        return min(use,lose)

    

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


