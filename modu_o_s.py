import os

def get_current_directory():
    print(os.getcwd())

def change_directory(path):
    return os.chdir(path)

def make_directory(foldername):
    return os.mkdir(foldername)

def make_directory_inside_directory(path):
    return os.makedirs(path)

def delete_empty_folder(foldername):
    return os.rmdir(foldername)

def delete_folder_inside_folder(path):
    return os.removedirs(path)

def list_of_files(path):
    print(os.listdir(path))
    return os.listdir(path)

def walk_throughout_dir(path):
    var = os.walk(path)
    for i in var:
        print(i)

def file_info(path):
    stats = os.stat(path)
    return stats

def file_name(path):
    return os.path.basename(path)

def touple_of_file_path(path):
    return os.path.split(path)

def check_existence_of_file(path):
    return os.path.exists(path)

def check_file_or_dirctory(path):
    return os.path.isfile(path)

def ab():
    return os.path.join()

def rename_folder_or_file(old,new):
    return os.rename(old,new)

def join_folder_and_file_path(folder,file):
    return os.path.join(folder,file)

def system():
    return os.system("dir")

def get_environment():
    return os.environ

def system_name():
    return os.name
