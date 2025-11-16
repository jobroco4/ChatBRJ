<<<<<<< HEAD
import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not os.path.isdir(full_path):
        raise ValueError('Error: {directory} is not a directory')
    elif os.path.abspath(full_path) != working_directory:
        raise ValueError('Error: Cannot list {directory} as it is outside the permitted working directory')
    else:
        files_info = []
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            if os.path.isfile(entry_path):
                files_info.append(f"- {entry}: file-size={os.path.getsize(entry_path)} bytes, is_dir=False")                
            elif os.path.isdir(entry_path):
                files_info.append(f"- {entry}: file-size={os.path.getsize(entry_path)} bytes, is_dir=True")
        return "\n".join(files_info)
    

print(get_files_info("../calculator", "pkg"))
=======
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
>>>>>>> 344eccd (added tests)
