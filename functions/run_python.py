import os
import subprocess

def run_python_file(working_directory, file_path, args=[]) -> str:
  abs_wd = os.path.abspath(working_directory)
  file_full_path = os.path.abspath(os.path.join(abs_wd, file_path))

  if not file_full_path.startswith(abs_wd):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  try:
    if not os.path.exists(file_full_path):
      return f'Error: File "{file_path}" not found.'

  except Exception as e:
    return f'Error: {e}'
  
  if not file_path.endswith('.py'):
    return f'Error: "{file_path}" is not a Python file.'

  try:
    
    completed_process = subprocess.run(
      ['python', file_full_path] + args
      , timeout=30
      , capture_output = True
      , text = True
      , cwd = working_directory
      )
  

    result = ''
    if len(completed_process.stdout) == 0 and len(completed_process.stderr) ==0:
      result += "No output produced"
    else: 
      result += f'STDOUT: \n{completed_process.stdout}'
      result += f'\nSTDERR: \n{completed_process.stderr}'

    if completed_process.returncode != 0:
      result += f'\nProcess exited with code {completed_process.returncode}'
    
  except Exception as e:
    return f'Error: executing Python file: {e}'
  
  return result