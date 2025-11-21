
def get_file_content(working_directory, file_path):
    import os
    from functions import config

    target_file_path = os.path.join(working_directory, file_path)
    if os.path.isabs(file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    elif not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    elif os.path.abspath(target_file_path).startswith(os.path.abspath(working_directory)) is False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    with open(target_file_path, "r") as file:
        content = file.read(config.MAX_CHARS)
        if len(content) == config.MAX_CHARS:
            content += f'\n[...File "{file_path}" truncated at 10000 characters]'
        
    return content

