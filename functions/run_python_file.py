import os 
import subprocess

def run_python_file(working_directory, filepath, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory) 
        target_file = os.path.abspath(os.path.join(abs_working_dir, filepath))
        is_valid = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        if not is_valid:
            return f'Error: Cannot execute "{filepath}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{filepath}"'

        if not filepath.endswith('py'):
            return f'Error: {filepath} is not a Python file'

        command = ['python', target_file] 
        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=abs_working_dir, text=True, capture_output=True, timeout=30)
        return format_result(result)

    except Exception as e:
        return f"Error: executing Python file: {e}"


def format_result(result):
    try:
        output = []
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        returncode = result.returncode
        if returncode != 0:
            output.append(f"Process exited with code {returncode}") 

        elif not (stdout or stderr):
            output.append("No output produced")

        output.extend(
                [
                    f"Command: {' '.join(result.args)}",
                    f"STDOUT:\n{stdout}",
                    f"STDERR:\n{stderr}"
                ]
        )

        return '\n'.join(output) 

    except Exception as e:
        return f"Error: executing Python file: {e}"
