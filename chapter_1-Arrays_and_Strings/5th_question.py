'''
there are three types of operations that can be performed on strings. insert a char,
delete a char, replace a char. given 2 strings, write a function to check if they are one edit 
or zero edits away
'''

#brute force approach, but this version is n
def one_away(str1: str,str2:str)-> bool:
    '''
    time complexity: O(n)
    space complexity : O(1)
    '''
    if str1 == str2:
        return True
    elif abs(len(str1)-len(str2))>1:
        return False
    if len(str1)> len(str2):
        str1,str2 = str2,str1
    index1 = index2 = 0
    found_difference = False
    while index1<len(str1) and index2<len(str2):
        if str1[index1] != str2[index2]:
            if found_difference:
                return False
            found_difference = True
            if len(str1) == len(str2):
                index1+=1
                
        else:
            index1+=1
        index2+=1
    return True

print(one_away('plek','pale'))
print(one_away('bale','pale'))

