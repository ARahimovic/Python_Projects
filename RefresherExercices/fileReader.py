def safe_file_opener(filename):
    try :
        with open(filename, "rt") as file:
            content = file.read()
            print(f"--- File Content --- \n{content}")
    
    except FileNotFoundError:
        print("File not found, creating a new one")
        with open(filename, "w") as file:
            file.write("New File intialsed")
    
    finally:
        print("Log attempt finished.")


if __name__ == "__main__" :
    fileName = "data.txt"
    safe_file_opener(fileName)
    
    print("\n--- Running a second time ---")
    safe_file_opener(fileName)


    