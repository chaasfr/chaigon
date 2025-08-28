import os

def get_files_info(working_directory, directory=".") -> str:
  results = ['Result for current directory:']  
  abs_wd = os.path.abspath(working_directory)
  directory_full_path = os.path.abspath(os.path.join(abs_wd, directory))

  if not directory_full_path.startswith(abs_wd):
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


