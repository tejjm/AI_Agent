import os
from config import MAX_CHAR
def get_file_content(working_directory, file_path):
    try:
        abs_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
        common_path = os.path.commonpath([abs_dir,abs_file_path])
        if not common_path == abs_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path,"r") as f:
            content = f.read(MAX_CHAR)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at 10000 characters]'

        return content
    
    except Exception as e:
        return f'Error: {e}'

