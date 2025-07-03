'''
question: write a method to replace all spaces in a string with '%20'. you may assume that the string has sufficient
space at the end to hold the additional characters and that you are given the true length of the string.
edge cases: empty string, no spaces, 
''' 
#brute force approach
#using slicing and concatination
def replace_str(string:str, len_of_str:int) -> bool:
    '''
    time complexity: O(n^2)
    space complexity: O(n)
    this approach is not efficient because we use forward replacement algorithm. Here for every replacement we have to shift all the elements 
    to right. so each operation would take O(n) time and in the end it would be O(n^2) and even we are creating multiple copies of string to store
    '''
    if len_of_str == 0:
        return 'Empty String'
    if ' ' not in string:
        return string
    for char in range(len_of_str):
        if string[char] == ' ':
            string = string[:char] + '%20' + string[char+1:]
    return string

print(replace_str('mr John Smith               ',13))

#efficient algorithm, use backward inplace replacement