import os
def run_python_file(working_directory, file_path, args=None):
        try:
            abs_work = os.path.abspath(working_directory)
            abs_file_path = os.path.abspath(os.path.join(abs_work, file_path))
            if os.path.commonpath([abs_work,abs_file_path]) != abs_work:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            if not os.path.isfile(abs_file_path):
                return f'Error: "{file_path}" does not exist or is not a regular file'
            if not abs_file_path.endswith('.py'):
                return f'Error: "{file_path}" is not a Python file'
            command = ["python", abs_file_path]
        
        except Exception as e:
             return f"Error: executing Python file: {e}"
