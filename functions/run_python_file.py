import os
import subprocess
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
            if args:
                command.extend(args)
            result = subprocess.run(
                 command,
                cwd=abs_work,       
                capture_output=True, 
                text=True,            
                timeout=30)
            output = []
            if result.returncode != 0:
                 output.append(f"Process exited with code {result.returncode}")
            if result.stderr:
                 output.append(f" STDERR: {result.stderr}")
            if result.stdout:
                output.append(f" STDOUT: {result.stdout}")
            elif not result.stderr and not result.stdout:
                 output.append(" No output produced")
            return "\n".join(output)
        except Exception as e:
             return f"Error: executing Python file: {e}"
    

                 
            

        















        except Exception as e:
             return f"Error: executing Python file: {e}"
