from json_read_write import *

if __name__ == '__main__':

  f_name = "matrix.json"
  data = read_json_file(f_name)

  print("data")
  print(data)
  print("data[matrix]")
  print(data["matrix"])

  mat = data["matrix"]

  for i in range(len(mat)):
    for j in range(len(mat[0])):
      print("mat",i,j)
      print(mat[i][j])
      mat[i][j] = mat[i][j] * 10
  
  print(data["matrix"])

  f_name = "matrix2.json"
  write_json_file(f_name, data)
