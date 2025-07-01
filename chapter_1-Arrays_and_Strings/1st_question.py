'''
question: implement an algorithm to determine if a string has all unique character.
what if you cannot use any additional datastructures
'''
string = 'barthfkfvvjkjkjkklkl'

# if string mutation is allowed
def is_unique(str: string)-> bool:
    '''
    time complexity: O(nlogn),because sorting algorithm is used.
    space complexity: O(1), because no additional space is used 
    '''
    if len(string)<=1:
        return True
    sort_str = sorted(string)
    for char in range(1,len(sort_str)):
        if sort_str[char] == sort_str[char-1]:
            return False
    return True
print(is_unique(string))

#if using additional data structure is allowed
def is_unique1(str: string) -> bool:
    if len(string)<=1:
        return True
    unique_list = []
    for char in string:
        if char not in unique_list:
            unique_list.append(char)
        else:
            return False
    return True

print(is_unique1(string))

string2 = 'helo'
# if both string manipulation and other data structures is not allowed
def is_unique2(string2: str)-> bool:
    '''
    time complexity: O(n**2)
    space complexity: O(1)
    '''
    if len(string2)<=1:
        return True
    for i in range(len(string2)-1):
        for j in range(i+1, len(string2)):
            if string2[i] == string2[j]:
                return False
    return True

print(is_unique2(string2))
