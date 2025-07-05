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
def urlify(string:str,true_length:int)->str:
    '''
    time complexity: O(n)
    space complexity : O(1)
    '''
    string = list(string)
    # get the count of spaces in string
    space_count = 0
    for i in range(true_length):
        if string[i] == ' ':
            space_count+=1
    #print('space count ',space_count)
    index = true_length + 2*space_count
    #print('index = ',index)

    for char in range(true_length-1,-1,-1):
        if string[char] == ' ':
            string[index-1] = '0'
            #print(string)
            string[index-2] = '2'
            #print(string)
            string[index-3] = '%'
            #print(string)
            index-=3
        else:
            string[index-1] = string[char]
            #print(string)
            index-=1
    #print(str(string))
    return string

string = urlify('mr John Smith               ',13)
print("".join(string))
