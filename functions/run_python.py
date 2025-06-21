import os
import subprocess



def run_python_file(working_directory, file_path):

    target_file = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))

    if not target_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path[-3:] == ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:

        result = subprocess.run(["python", target_file], capture_output=True, text=True, timeout=30, check=True)

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"
    
    return "\n".join(output) if output else "No output produced."

