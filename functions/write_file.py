import os
def write_file(working_directory, file_path, content) -> str:
  abs_wd = os.path.abspath(working_directory)
  file_full_path = os.path.abspath(os.path.join(abs_wd, file_path))

  if not file_full_path.startswith(abs_wd):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  if os.path.exists(file_full_path) and os.path.isdir(file_full_path):
        return f'Error: "{file_path}" is a directory, not a file'
    
  try:
    if not os.path.exists(os.path.dirname(file_full_path)):
      os.makedirs(os.path.dirname(file_full_path))
  

    with open(file_full_path, "w") as f:
      f.write(content)

  except Exception as e:
    return f'Error: {e}'
  

  return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'