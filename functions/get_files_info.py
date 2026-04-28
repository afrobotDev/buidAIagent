import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        is_valid = os.path.commonpath([abs_working_dir,target_dir]) == abs_working_dir

        if not is_valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: {directory} is not a directory'

        def iterate_over_dir(target_dir): 
            contents_target_dir = os.listdir(target_dir) 
            for content in contents_target_dir: 
                full_path = os.path.join(target_dir, content) 
                is_dir = os.path.isdir(full_path) 

                if is_dir:
                    return iterate_over_dir(full_path) 

                if os.path.isfile(content):
                    file_size = os.path.getsize(content) 
                    return f'{content}: file_size={file_size} bytes, is_dir={is_dir}'
    

    except Exception as e:
        return f"Error: {e}"
