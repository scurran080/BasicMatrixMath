###Sean Curran
###October 2019
###A program to do simple matrix math I made to speed up doing my homework
###S

#add one matrix to another
def add_matrix(a, b):
   if len(a) != len(b) or len(a[0]) != len(b[0]):
      return
   new_matrix = [[None for _ in range(len(a[0]))] for _ in range(len(a))]
   for i in range(len(a)):
      for x in range(len(a[0])):
         new_matrix[i][x] = (a[i][x] + b[i][x])
   return new_matrix

#subtract on matrix from the other
def subtract_matrix(a,b):
   if len(a) != len(b) or len(a[0]) != len(b[0]):
      return
   new_matrix = [[None for _ in range(len(a[0]))] for _ in range(len(a))]
   for i in range(len(a)):
      for x in range(len(a[0])):
         new_matrix[i][x] = (a[i][x] - a[i][x])
   return new_matrix

#Swap the position of two specified rows
#positions start at ZERO
def swap_row(matrix,row_index1, row_index2):
   if row_index1 < 0 or row_index2 < 0 or row_index1 > (len(matrix) - 1) or row_index2 > (len(matrix) - 1):
      return
   temp = matrix[row_index1]
   matrix[row_index1] = matrix[row_index2]
   matrix[row_index2] = temp
   return matrix

#Either multiply or divide a specified row by a certain amount for row operations.
#positions start at ZERO
def scale_row(matrix,row,operation,value):
   if row < 0 or row > (len(matrix) - 1):
      return
   if operation == "mul":
      for i in range(len(matrix[0])):
        matrix[i][row] = (matrix[i][row] * value)
      return matrix

   if operation == "div":
      if value == 0:
         return
      for i in range(len(matrix[row])):
         matrix[i][row] = matrix[i][row] / value
      return matrix

#Returns the specified vector based on its index within the matrix that is passed to it.
#Positioning starts at ZERO
def get_vector(matrix, vecPos):
   temp = matrix[vecPos]
   return temp

def print_matrix(matrix):
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         print(matrix[i][j], end ="  ")
      print("\n")

def multiply_matrix(matrixA, matrixB):
   result = [[0 for i in range(len(matrixB[0]))] for j in range(len(matrixA))]
   for i in range(len(matrixA)):
      for j in range(len(matrixB[0])):
         for k in range(len(matrixB)):
            result[i][j] += matrixA[i][k] * matrixB[k][j]
   return result

