print('help me nice people, help me rob a store ;))))))))))))))))))))))))))))))))))))))))))))')

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
      ]
 
print(matrix)
print(matrix[0])
print(matrix[0][2])
# first [ ] is row second is column
print(matrix[1][1])
# to change value
matrix [0][1] = 20
print(matrix[0][1])

for row in matrix:
  print (row[2])

for row in matrix:  #this will itterate over 3 items i.e here 3 rows
  for item in row:   #this will iterate over items in a row i.e. for row 1===1,2,3
    print(item)