import json; import subprocess; import sys; import time; import os; import CustomErrors as ce 

frames = [
    r"""
        🌱
    """,
    r"""
        🌱
        │
    """,
    r"""
        🌱
        │
       / \
    """,
    r"""
        🌱
        │
       / \
      /   \
    """,
    r"""
        🌳
        │
       / \
      /   \
     /_____\
    """,
]

for frame in frames:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame)
    time.sleep(0.4)

print(r''' ██████╗ █████╗ ███╗   ███╗
██╔════╝██╔══██╗████╗ ████║
██║     ███████║██╔████╔██║
██║     ██╔══██║██║╚██╔╝██║
╚██████╗██║  ██║██║ ╚═╝ ██║
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝                   
''')



for i in range(100000000000000000000000000000000000000000000000000000):
    command = input("\nEnter command here: ")



    #syntax:
    #all commands should start with "cam"

    if command == "cam package":
        filename = input("Enter the file's name here: ")
        version = input("Enter the file's version here (ie 0.1): ")
        req = input("What does your file require to run? ")
        lang = input("What programming language was this written in? ")
        langversion = input("What version of the programming language that was used to write the file did you use? ")

        author = input("Who wrote the file? ")
        print("Packaging file...")
        data = {            #defines the data obj
            "name": filename,
            "version": version,
            "author": author,
            "requirements": req,
            "engine":
            {
                "language": lang,
                "language_version": langversion
            }
        }

        with open(f"{filename}.json", "w") as f:
            json.dump(data, f, indent=4)    #creates the file
        print("File generated!")

    elif command == "cam upd": 
        filename = input("Enter the file's name here: ")
        version = input("Enter the file's new version here (ie 0.1): ")
        author = input("Who wrote the file? ")
        req = input("What does your file require to run? ")
        lang = input("What programming language was this written in? ")
        langversion = input("What version of the programming language that was used to write the file did you use? ")

        data = {        #redefines the data obj (in this file there is no difference between the upd data and the package data bc upd edits the values of each variable not obj's struct)
            "name": filename,
            "version": version,
            "author": author,
            "requirements": req,
            "engine":
            {
                "language": lang,
                "language_version": langversion
            }
        }
        with open(f"{filename}.json", "w") as f:
            json.dump(data, f , indent=4)
        print("File updated!")

    elif command == "cam inst":
        lib = input("What would you like to install? ")
        subprocess.run(["pip", "install", lib])
        print("Package installed!")

    elif command == "cam del":
        lib = input("What library would you like to uninstall? ")
        subprocess.run(["pip3", "uninstall", lib])  #Requires pip

    elif command == "cam open":
        filename = input("What file would you like to open? ")
        try:
            with open(f"{filename}.json", "r") as f:
                data = json.load(f) #reads json file as Python dict
            print(data)
        except FileNotFoundError:
            print("That file does not exist!")

    #elif command == "cam terminal":
        #print("Welcome to Cam's built in terminal!")
        #tcommand = input("> ")
        #tcommandf = tcommandu = print(tcommand, sep=",")
        #subprocess.run(tcommandu)

    elif command == "cam view error log":
        with open("errorlog.txt", "r") as f:
            print(f.readlines)

    elif command == "exit":
        sys.exit("Session ended")

    else:
        print("That is an invalid command.")
        print("ERROR CODE: 401 Invalid input")
        ce.uce
        with open("errorlog.txt", "a") as f:
            f.write(f"{ce.uie}\n")
