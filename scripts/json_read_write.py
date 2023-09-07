import json
import os

def read_json_file(file_name):
  if os.path.exists(file_name):
    with open(file_name, 'r') as f:
      json_load = json.load(f)
      return json_load, True
  return None, False

def write_json_file(file_name, dict_data):
  with open(file_name, 'w') as f:
    json.dump(dict_data, f, indent=2)

if __name__ == '__main__':

  print(json.__version__)

  f_name = "test.json"
  data, read_sucess = read_json_file(f_name)

  if read_sucess == False:
    print("cannot find file")
    data = {'a': '10', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6'}
    write_json_file(f_name, data)

  else:

    new_data = {"a":"10"}
    data.update(new_data)

    new_data = {"f":"6"}
    data.update(new_data)

    f_name = "test2.json"

    write_json_file(f_name, data)
