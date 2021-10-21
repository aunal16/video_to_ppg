import os

def check_if_saved_before(folder: str, file: str) -> str, bool:
    check = True
    
    path = os.path.join(folder, file)
    # remove file extension from folder name
    path = os.path.splitext(path)[0]

    # check whether exists
    exists = os.path.isdir(path)
    if not exists:
        os.mkdir(path)
        check = False

    return [foldername, check]
