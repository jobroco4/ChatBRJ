from google import genai
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)



def get_files_info(working_directory, directory="."):
    import os

    target_directory = os.path.join(working_directory, directory)
    if directory == ".":
        target_directory = working_directory
    elif os.path.isabs(directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.exists(target_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'
    elif os.path.abspath(target_directory).startswith(os.path.abspath(working_directory)) is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    files_info = ""

    for entry in os.scandir(target_directory):
        if entry.is_file():
            files_info += f'- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir=False\n'
        elif entry.is_dir():
            files_info += f'- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir=True\n'


    return files_info

