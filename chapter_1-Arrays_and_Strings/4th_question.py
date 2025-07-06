'''
question: given a string, write a function to check if it is a permutation of a palindrome.
example:
input: Tact Coa
output: True   #(the palindrome of input is 'atco cta')
Note: Non-letter characters are not required, CASE insensitive
'''
# by using hash table/dictionary
def permutation_palindrome(string:str) -> bool:
    '''
    time complexity=O(n)
    space complexity= O(N)
    '''
    string = string.lower().replace(' ','')
    odd_count = 0
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for item in char_count:
        if char_count[item] %2 == 1:
            odd_count+=1
        if odd_count>1:
            return False
    return True

print(permutation_palindrome('tact coa'))

#this problem can also be solved using Bit manipulation

