import os

def write_file(working_directory, file_path, content):
    target_file = os.path.join(os.path.abspath(working_directory), file_path)

    if not target_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(target_file, "w") as f:
            f.write(content)
            f.close()
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
