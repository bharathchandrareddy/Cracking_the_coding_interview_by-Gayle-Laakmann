'''
implement a method to perform basic string compressions using the counts of repeated characters.
for example str = aabcccccaaa would become a2b1c5a3. if compressed string larger or equal to input str, return input string
exaple:
input = aabcccccaaa
output: a2b1c5a3
'''

# this is the brute force and most optimal solution
def compressed_string(string:str)->str:
    '''
    time complexity: O(n)
    space complexity: O(n)
    '''
    if len(string) <= 1:
        return string
    compressed = []
    count =1
    for char in range(1,len(string)):
        if string[char] == string[char-1]:
            count+=1
        else:
            compressed.append(string[char-1]+str(count))
            count = 1
    compressed.append(string[-1]+ str(count))
    if len(compressed) >= len(string):
        return string
    
    return ''.join(compressed)
print(compressed_string("b"))
