import subprocess

if __name__ == '__main__':
    print("Choose the interface. CLI / Web Interface.")
    print("1 | cli | CLI --> CLI")
    print("2 | web | WEB--> Web Interface")
    print("Any other key --> Terminate Program")
    choice = input("Interface: ")

    match choice:
        case "1" | "cli" | "CLI":
            print("Starting CLI...")
            subprocess.run(["python", "./cli.py"])
        case "2" | "web" | "WEB":
            print("Starting Web Interface...")
            subprocess.run(["streamlit", "run", "./app.py"])
        case _:
            print("Program Terminated")
            exit()
