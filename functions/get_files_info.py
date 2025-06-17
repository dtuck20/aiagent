import os


def get_files_info(working_directory, directory=None):



    #if directory is outside of working directory return error string:
    #print(os.path.join(os.path.abspath(working_directory), directory))
    target_dir = os.path.join(os.path.abspath(working_directory), directory)

    if not target_dir.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        contents = os.listdir(target_dir)
    except Exception as e:
        return f'Error: {e}'


    output = []
    try:
        for item in contents:
            output.append(f'- {item}: file_size={os.path.getsize(os.path.join(target_dir,item))}, is_dir={os.path.isdir(os.path.join(target_dir,item))}')
    except Exception as e:
        return f'Error: {e}'

    return "\n".join(output)