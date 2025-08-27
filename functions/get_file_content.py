import os
from functions import config

def get_file_content(working_directory, file_path) -> str:
  abs_wd = os.path.abspath(working_directory)
  file_full_path = os.path.abspath(os.path.join(abs_wd, file_path))

  if not file_full_path.startswith(abs_wd):
    return f'Error: Cannot read "{file_full_path}" as it is outside the permitted working directory'
  
  if not os.path.isfile(file_full_path):
    return f'Error: File not found or is not a regular file: "{file_full_path}"'

  try:
    with open(file_full_path, "r") as f:
      result = f.read(config.MAX_CHARS_PER_FILE)

    if len(result) == config.MAX_CHARS_PER_FILE:
      result += f'\n[...File "{file_full_path}" truncated at 10000 characters]'
  except Exception as e:
    return f'Error: {e}'
 
  return result