import os 
import subprocess

def get_file_content(working_directory, filepath, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory) 
        target_file = os.path.abspath(os.path.join(abs_working_dir, filepath))
        is_valid = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        if not is_valid:
            return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{filepath}"'

        if not filepath.endswith('py'):
            return f'Error: {filepath} is not a Python file'

        command = ['python', target_file] 
        command.extend(args)

        result = subprocess.run(command, cwd=abs_working_dir, text=True, cupture_output=True, timeout=30)

        def format_result(result):

            stdout = result.stdout.strip()
            stderr = result.stderr.strip()

            if result.returncode != 0:
                stdout = " " 

            return(

                    f"Command: {' '.joint(result.args)}\n"
                    f"Exit code: {result.returncode}\n"
                    f"STDOUT:\n{stdout}\n"
                    f"STDERR:\n{stderr}"

            )
                



    except Exception as e:
        return f"Error: {e}" 

