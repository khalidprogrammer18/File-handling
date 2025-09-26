import os
import glob
import shutil
from pathlib import Path
from os import path
import subprocess

class system:
    
    def __init__(self, file):
        result = []
        for full_path, directories, apps in os.walk(r"C:\Users\acer"):
            for directory in directories:
                if directory.lower() == file.lower():
                    result.append(f"{full_path}\\{directory}")
            for app in apps:
                if app.lower() == file.lower():
                    result.append(f"{full_path}\\{app}")
        if len(result) == 1:
            self.file = result[0]
        elif len(result) == 0:
            raise FileNotFoundError("This file is not exists")
        else:
            print(f"We found {len(result)} result found, please choose one")
            for num, r in enumerate(result):
                print(f"{num+1}- {r}")
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    self.file = result[choice-1]
                    break
                except:
                    if len(result) == 2 and choice not in range(1,len(result)):
                        print(f"You must choose 1 or 2")
                    else:
                        print(f"You must choose a number between 1 and {len(result)}")

    def getter(self):
        return self.file

    def setter(self, new_file):
        self.file = system(new_file)

    def __str__(self):
        return str(self.file)

    def open_file(self, file):
        my_list = [e.name for e in Path(self.file).iterdir()]
        if file in my_list:
            self.file = path.join(self.file, file)
        else:
            raise FileNotFoundError

    def back(self):
        path_list = str(self.file).split("\\")
        self.file = "\\".join(path_list[0:-1])

    def show(self):
        return " - ".join(os.listdir(self.file))

    def Rename(self, new_name):
        Path(self.file).rename(path.join("\\".join(str(self.file).split("\\")[:-1]), new_name))

    def delete(self):
        shutil.rmtree(str(self.file))

    def search(self, file):
        return " - ".join([file for file in glob.iglob(f"**/*{file}", recursive=True)]) if len([file for file in glob.iglob(f"**/*{file}", recursive=True)]) != 0 else "The is no result"
    
    def make(self, file):
        Path(path.join(self.file, file)).mkdir()

    def move(self, file, dir):
        shutil.move(path.join(self.file, file), path.join(self.file, dir))

    def ReadFile(self, name):
        with open(path.join(self.file,name), "r") as file:
            return file.read()

    def OverWriteFile(self, name, text):
        concat = path.join(self.file,name)
        if Path.exists(Path(concat)):
            with open(concat, "w") as file:
                file.write(text)
        else:
            if input("File is not exists, Do you want to create it? (Y/N): ") == "Y":
                with open(concat, "w+") as file:
                    file.write(text)

    def AppendFile(self, name, text):
        concat = path.join(self.file,name)
        if Path.exists(Path(concat)):
            with open(concat, "a") as file:
                file.write(text)
        else:
            if input("File is not exists, Do you want to create it? (Y/N): ") == "Y":
                with open(concat, "a+") as file:
                    file.write(text)

    def HowMany(self):
        my_list = os.listdir(self.file)
        direc, file = 0, 0
        for l in my_list:
            if Path(path.join(self.file, l)).is_dir():
                direc += 1
            else: 
                file += 1
        return f"Result {len(my_list)} contain {direc} directories and {file} files"

    def Copy(self, file, CopyName):
        shutil.copy(path.join(self.file, file), path.join(self.file, CopyName))

    def run(self):
        return subprocess.run(["python", self.file], capture_output=True, text=True)

if __name__ == "__main__":
    
    print("Wellcome to file manegment. Start with opening a folde")

    while True:
        filechoie = input("Enter a file name: ").strip()
        try:
            USER = system(filechoie)
            break
        except:
            print(f"{filechoie} file is not exists!")

    print(f"Right, Now you can access this folder by thease comands")

    while True:

        print(f"""
  ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗
  ║ 1- change the folder        2- get full path            3- open file            4- close current file   ║
  ║ 5- display all files        6- rename a file            7- run a python file    8- search in the folder ║
  ║ 9- make a folder            10- move file to folder     11- read a file         12- overwrite a file    ║
  ║ 13- append/create file      14- files counter           15- copy a file         16- close               ║
  ║ Path: {str(USER.getter()).ljust(98)}║
  ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            """)

        while True:
            try:
                choice = int(input("choose a command: "))
                if choice not in range(1,17):
                    raise ValueError
                break
            except:
                print("You should choose a number between 1 to 16")

        if choice == 1:
            try:
                file1 = input("choose another folder or file or (b) to back: ")
                if file1.lower().strip() == "b":
                    continue
                USER.setter(file1)
                print(f"File chaanged to {file1}")
                continue
            except:
                print(f"{file1} file is not exists")

        elif choice == 2:
            print("Full path:", USER.getter())

        elif choice == 3:
            try:
                file2 = input("Choose a file to open or (b) to back: ")
                if file2.lower().strip() == "b":
                    continue
                USER.open_file(file2)
                print(f"{file2} is opened")
                continue
            except:
                print(f"{file2} file is not exists")

        elif choice == 4:
            if USER.getter() == r"C:\Users\acer":
                print("Can not close 'acer'")
                continue
            USER.back()
            print("The current file has been closed!")

        elif choice == 5:
            if Path(USER.getter()).is_dir():
                print(USER.show())
            else:
                print("Only can show directories containers")

        elif choice == 6:
            try:
                New_name = input("Write the new name or (b) to back: ")
                if New_name.lower().strip() == "b":
                    continue
                USER.Rename(New_name)
                print(f"file name changed from {str(USER.getter()).split("\\")[-1]} to {New_name}")
                USER.setter(New_name)
                continue
            except:
                print("This name is not allow")

        elif choice == 7:
            print(USER.run().stdout.strip())

        elif choice == 8:
            print(USER.search(input("Write a filter: ")))

        elif choice == 9:
            USER.make(input("Write file name: "))

        elif choice == 10:
            try:
                file10 = input("Write the file name: ")
                dir10 = input("Write the directory name: ")
                USER.move(file10, dir10)
                print(f"{file10} has been moved to {dir10}")
            except:
                print("Invalid input")

        elif choice == 11:
            try:
                file11 = input("Write the file name: ")
                print(USER.ReadFile(file11))
            except:
                print(f"{file11} file is not exists!")

        elif choice == 12:
            try:
                file12 = input("Write the file name: ")
                text12 = input("Alright! start typing: ")
                USER.OverWriteFile(file12, text12)
            except:
                print(f"{file12} file is not exists!")

        elif choice == 13:
            try:
                file13 = input("Write the file name: ")
                while True:
                    text13 = input("start typing or (-c) to close: ")
                    if text13 == "-c":
                        break
                    USER.AppendFile(file13, f"{text13}\n")
            except:
                print("Something went wrong")

        elif choice == 14:
            print(USER.HowMany())

        elif choice == 15:
            try:
                file15 = input("Write the file name: ")
                copy15 = input("Write the copy name: ")
                USER.Copy(file15, copy15)
                print(f"{file15} file has been copied to {copy15}")
            except:
                print(f"{file11} file is not exists!")

        else:
            exit()