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