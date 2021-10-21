import os

def check_if_saved_before(frame_dir: str,vid_name: str) -> list:
    check = True
    
    path = os.path.join(frame_dir, vid_name)
    # remove file extension from folder name
    path = os.path.splitext(path)[0]

    # check whether exists
    exists = os.path.isdir(path)
    if not exists:
        os.mkdir(path)
        check = False

    return [path, check]
