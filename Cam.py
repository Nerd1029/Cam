import json; import subprocess; import sys

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
        lang = input("What programming language was this written in? ")
        langversion = input("What version of the programming language that was used to write the file did you use? ")

        author = input("Who wrote the file? ")
        print("Packaging file...")
        data = {            #defines the data obj
            "name": filename,
            "version": version,
            "author": author,
            "engine":{
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
        lang = input("What programming language was this written in? ")
        langversion = input("What version of the programming language that was used to write the file did you use? ")

        data = {            #redefines the data obj
            "name": filename,
            "version": version,
            "author": author,
            "engine":{
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
        subprocess.run(["pip3", "uninstall", lib])

    elif command == "cam open":
        filename = input("What file would you like to open? ")
        with open(f"{filename}.json", "r") as f:
            data = f.readlines()
        print(data)

    elif command == "exit":
        sys.exit("Session ended")

    else:
        print("That is an invalid command.")
        print("ERROR CODE: 400")