from google.genai import types
import function_declaration as fd

available_functions = types.Tool(
    function_declarations=[fd.schema_get_files_info,
                           fd.schema_get_file_content,
                           fd.schema_run_python_file,
                           fd.schema_write_file],
)
