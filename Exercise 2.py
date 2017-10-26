#------------Exercise 2-----------------#
'''
1. Find the total number of elements in a matrix
2. Flat the matrix
3. Transpose the matrix 

Hints:
Use double 'for' loops

'''

#------------Solution 2-----------------#

Matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
total_num = sum(len(x) for x in Matrix)                                  # find the total number of elements
print ('Total element number :', total_num)

M_Flat = [e[i] for e in Matrix for i in range(len(Matrix[0]))]           # Flat the matrix
print ('Elements in Matrix : ', M_Flat)

M_transpose = [[e[i] for e in Matrix] for i in range(len(Matrix)-1)]     # Find the transpose    
print ('Transpose of Matrix :', M_transpose)