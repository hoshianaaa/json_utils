from json_read_write import *

if __name__ == '__main__':

  f_name = "matrix.json"
  data, read_success = read_json_file(f_name)

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
  
  new_data = {"matrix":mat}
  print(new_data)

  f_name = "matrix2.json"
  write_json_file(f_name, new_data)
