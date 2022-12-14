import os
import hashlib
import json
import shutil

#Find all ts files in the repository

def find_files():
    ts_files=[]
    exclude = set(["node_modules"])
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude]
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
    #file_hash=""
    #with open(file, "rb") as f:
        #file_hash = hashlib.md5(f.read()).hexdigest()
    #if file in hashes and hashes[file] == file_hash:
        #return False
    #else:
        #hashes[file] = file_hash
        #with open("./hashes.json", "w") as json_file:
            #json.dump(hashes, json_file)
        #command = f"tsc {file}"
        #print("compiling; ", file)
        #os.system(f"{command}")
    file = file.replace("\\", "/")
    return f"{file[2:-3]}.js"

#save files in a folder lambda

def order_files(file):
    print(file)
    try:
        os.mkdir(f"./lambda/{'/'.join(file.split('/')[:-1])}")
    except:
        pass
    shutil.move(file, f"./lambda/{file}")

#main 

#hashes = {}
#if not os.path.exists("./hashes.json"):
    #with open("./hashes.json", "w") as json_file:
        #json.dump({}, json_file)
#with open("./hashes.json", "r") as json_file:
    #hashes = json.load(json_file)

files = find_files()
os.system(f"tsc")
for file in files:
    compiled_file = compile(file)
    if compiled_file:
        order_files(compiled_file)
