from json_read_write import *

if __name__ == '__main__':

  f_name = "test.json"
  data = read_json_file(f_name)

  new_data = {"a":"10"}
  data.update(new_data)

  new_data = {"f":"6"}
  data.update(new_data)

  f_name = "test2.json"

  write_json_file(f_name, data)
