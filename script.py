import os

#Find all ts files in the repository

def find_files(path):
    directories=[]
    files=[]
    base_directory_files = os.listdir(path)
    for item in base_directory_files:
        if item == ".git": continue
        if os.path.isdir(item):
            directories.append(item)
    #print(directories)
    for dir in directories:
        for file in os.listdir(f"{path}/{dir}"):
            if file[-3:] == ".ts":
                files.append(f"{dir}/{file}")
    #print(files)
    return  files

#run tsc file_path/file_name on every ts file

def compile(file):
    command = f"tsc {file}"
    os.system(f"cmd /c {command}")


files = find_files(".")
for file in files:
    compile(file)