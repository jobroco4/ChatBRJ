from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes the selected content to a file in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory.",
                )     
        },
    ),
)

def write_file(working_directory, file_path, content):
    import os
    from functions import config

    target_file_path = os.path.join(working_directory, file_path)
    if os.path.isabs(file_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif os.path.abspath(target_file_path).startswith(os.path.abspath(working_directory)) is False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(target_file_path):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        with open(target_file_path, "w") as file:
            file.write(content[:config.MAX_CHARS])


    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'