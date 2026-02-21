from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description="Returns the content in the file for which path was given, if the content has more than 10000 characters it gets truncated at that",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="This is the path given to file which we are looking to find"
            ),
            },
        required=["file_path"]
    )
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given content to the file located at given file path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="File path for file on which writing operation needed to be done"
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="Content which needs to be written to the given file path"
            )},
        required=["file_path","content"]
        
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description="Runs a python file and returns a output/error list",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
            type=types.Type.STRING,
            description="This is the path given to file which we are looking to find"
            ),
            "args":types.Schema(
                type=types.Type.ARRAY,
                items = types.Schema(type=types.Type.STRING),
                description="Arguments which are passed down to the python file"
            )
            },
        required=["file_path"]
        )
    )




