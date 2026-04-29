import os 
from config import MAX_CHARS


def get_file_content(working_directory, filepath):
    try:
        abs_working_dir = os.path.abspath(working_directory) 
        target_file = os.path.abspath(os.path.join(abs_working_dir, filepath))
        is_valid = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        if not is_valid:
            return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{filepath}"'

        with open(target_file, 'r', encoding='UTF-8') as f:
            content = f.read(MAX_CHARS) 
            if f.read(1):
                content += f'[...Fi le "{filepath}" truncated at {MAX_CHARS} characters]'

            return content



    except Exception as e:
        return f"Error: {e}" 
