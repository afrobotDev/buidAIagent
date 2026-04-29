import os 


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
            new_content = f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



    except Exception as e:
        return f"Error: {e}" 

