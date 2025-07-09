'''
question: convert a given NxN matrix size image to 90 degrees
input:[[1,2,3][4,5,6][7,8,9]]
'''
def matrix_convert(matrix:list[list[int]])->None:
    '''
    time_complexity = O(n^2)
    space_complexity = O(1)
    '''
    l,r = 0,len(matrix) - 1
    while l < r:
        for i in range(r-l):
            top, bottom = l, r

            #save the top left as temp
            top_left = matrix[top][l+i]
            
            #move bottom left into top left
            matrix[top][l+ i] = matrix[bottom -i][l]

            #move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            #move top righht into bottom right
            matrix[bottom][r -i] = matrix[top + i][r]

            #move top left into top right
            matrix[top +i][r]= top_left
        
        r-=1
        l +=1
    return matrix

print(matrix_convert([[1,2,3],[4,5,6],[7,8,9]]))   

