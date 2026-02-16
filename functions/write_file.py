import os
def write_file(working_directory, file_path, content):
    try:
        abs_work = os.path.abspath(working_directory)
        abs_file_path = os.path.join(working_directory,os.path.abspath(file_path))
        if not os.path.commonpath([abs_work,abs_file_path]) == abs_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent = os.path.dirname(abs_file_path)
        os.makedirs(parent,exist_ok=True)
        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error:{e}"
    