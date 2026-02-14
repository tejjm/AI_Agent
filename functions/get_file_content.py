import os
def get_file_content(working_directory, file_path):
    abs_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    common_path = os.path.commonpath(abs_dir,abs_file_path)
    if not common_path == abs_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
    