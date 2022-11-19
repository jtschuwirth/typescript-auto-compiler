import os

#Find all ts files in the repository

def find_files():
    ts_files=[]
    for root, dirs, files in os.walk("."):
        for name in files:
            file = os.path.join(root, name)
            if file[-3:] == ".ts":
                ts_files.append(os.path.join(root, name))
        for name in dirs:
            file = os.path.join(root, name)
            if file[-3:] == ".ts":
                ts_files.append(os.path.join(root, name))
        
    return ts_files

#run tsc file_path/file_name on every ts file

def compile(file):
    command = f"tsc {file}"
    os.system(f"{command}")


files = find_files()
for file in files:
    compile(file)