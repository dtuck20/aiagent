import os


def get_file_content(working_directory, file_path):

    max_chars = 10000
    target_file = os.path.join(os.path.abspath(working_directory), file_path)

    if not target_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > max_chars:
                return f'{file_content_string[:max_chars]} [...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f'Error: {e}'