from google.genai import types
import function_declaration as fd

available_functions = types.Tool(
    function_declarations=[fd.schema_get_files_info,
                           fd.schema_get_files_content,
                           fd.schema_run_python,
                           fd.schema_write_file],
)
