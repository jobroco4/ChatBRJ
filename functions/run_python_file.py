def run_python_file(working_directory, file_path, args=[]):
    import os
    import subprocess
    import sys
    from functions import config

    target_file_path = os.path.join(working_directory, file_path)
    if os.path.isabs(file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif os.path.abspath(target_file_path).startswith(os.path.abspath(working_directory)) is False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(target_file_path):
        return f'Error: File "{file_path}" not found.'
    elif os.path.isfile(target_file_path):
        _, extension = os.path.splitext(file_path)
        if extension.lower() != ".py":
            return f'Error: File "{file_path}" is not a Python file.'
        else:    
            args = [sys.executable, target_file_path] + args
            print(args)
            result = subprocess.run(args , timeout=30, capture_output=True, text=True, cwd=None)
            if result.returncode == 0:
                return f'STDOUT: {result.stdout} STDERR: {result.stderr}'
            elif not result.stdout and not result.stderr:
                return 'No output produced.'
            elif result.returncode != 0:
                return f'Process exited with code {result.returncode} STDOUT: {result.stdout} STDERR: {result.stderr}'
            elif result.exception:
                return f'Error: executing Python file: "{file_path}"'
        