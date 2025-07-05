'''
question: given two strings, write a method to decide if one is a permutation of the other
edge cases: white space, unicode, capitalization
'''
#if string mutation is allowed
def check_permutation(string1:str,string2:str) -> bool:
    '''
    time complexity: O(nlogn)
    Space complexity: O(n)
    '''
    string1 = string1.lower().replace(' ','')
    string2 = string2.lower().replace(' ','')
    if len(string1) != len(string2):
        return False
    sort_str1 = sorted(string1)
    sort_str2 = sorted(string2)
    if sort_str1 == sort_str2:
        return True
    return False
    
print(check_permutation('hello world','hel lo w o r l d'))

#better time complexity
def check_permutation_2(string1:str,string2:str) -> bool:
    '''
    time complexity: O(n)
    space complexity: O(n)
    '''
    
    string1 = string1.lower().replace(' ','')
    string2 = string2.lower().replace(' ','')
    if len(string1) != len(string2):
        return False 
    dict={}
    for char in string1:
        if char in dict:
            dict[char] +=1
        else:
            dict[char] = 1
    for char in string2:
        if char not in dict:
            return False
        else:
            dict[char] -= 1
            if dict[char] < 0:
                return False
    return True
print(check_permutation_2('hello world','hel lo w o r l d'))


