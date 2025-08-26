import os
from functions import config

def get_files_info(working_directory, directory=".") -> str:
  results = ['Result for current directory:']  
  directory_full_path = os.path.abspath(os.path.join(working_directory, directory))

  if working_directory not in directory_full_path:
   results.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
   return "\n".join(results)
  
  if not os.path.isdir(directory_full_path):
   results.append(f'Error: "{directory}" is not a directory')
   return "\n".join(results)

  try:
    for e in os.listdir(directory_full_path):
      e_full_path = f'{directory_full_path}/{e}'
      e_size = os.path.getsize(e_full_path)
      e_is_dir = os.path.isdir(e_full_path)
      results.append(f' - {e}: file_size={e_size} bytes, is_dir={e_is_dir}')
  except Exception as e:
    return f'Error: {e}'
  
  return "\n".join(results)

def get_file_content(working_directory, file_path) -> str:
  file_full_path = os.path.abspath(os.path.join(working_directory, file_path))

  if working_directory not in file_full_path:
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