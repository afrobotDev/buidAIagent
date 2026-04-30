import os 
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file at the specified path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
    ),
)


def write_file(working_directory, filepath, content):
    try:
        abs_working_dir = os.path.abspath(working_directory) 
        target_file = os.path.abspath(os.path.join(abs_working_dir, filepath))
        is_valid = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        if not is_valid:
            return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{filepath}" as it is a directory'

        parent_dir = os.path.dirname(target_file)
        if not parent_dir:
            os.makedirs(parent_dir, exist_ok=True)


        with open(target_file, 'w', encoding='UTF-8') as f:
            f.write(content)
            return f'Successfully wrote to "{filepath}" ({len(content)} characters written)'



    except Exception as e:
        return f"Error: {e}" 

