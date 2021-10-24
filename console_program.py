import os
def dirlist(path):
    cnt = 0
    l = str(os.listdir(path))
    m = l[1:len(l)-1]
    for i in m.split(","):
        print(i)
        cnt = cnt + 1
    print(cnt)


def changedir(comm):
    os.chdir(comm)
    print("Directory changed")

def create_new_file(filename):
    f = open(filename,"w")
    print(f"{filename} named file created successfully")
    f.close()

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("file removed")
    else:
        print("File doesn't exits")

def folder_del(foldername):
    if os.path.exists(foldername):
        os.rmdir(foldername)
        print("folder removed")
    else:
        print("Folder doesn't exists")

def open_file(filename):
    f = open(filename,"r")
    x = f.read()
    f.close()
    print(x)

while True:
    command = input("$ ")
    if command[0:2]=="ls":
        path = command[3:]
        if path=="":
            dirlist(None)
        else:
            dirlist(path)
    elif command[0:2]=="cd":
        comm = command[3:]
        changedir(comm)
    elif command == "whoami":
        print(os.getlogin())
    elif command == "pwd":
        print(os.getcwd())
    elif command[0:5]=="touch":
        create_new_file(command[6:])
    elif command[0:3]=="del":
        delete_file(command[4:])
    elif command[0:3]=="cat":
        open_file(command[4:])
    elif command[0:5]=="rmdir":
        folder_del(command[6:])
    elif command[0:5]=="mkdir":
        os.mkdir(command[6:])
        print("folder created successfully")
    elif command[0:4]=="copy":
        x,y = command[5:].split(" ")
        f = open(x,"r")
        co = f.read()
        f = open(y,"w+")
        f.write(co)
        f.close()
        print("text copied successfully")

    
    elif command=="exit":
        exit()
    elif command=="logout":
        print("logging out...")
        break
    else:
        print("Invalid command!")
        
    
