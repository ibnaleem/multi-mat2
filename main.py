import os, sys, subprocess

file_extention = input(str("Enter file extention: "))
current_directory = os.getcwd()
cleaned_directory = os.path.join(current_directory, "cleaned")

def clean_files():

    try:
        os.makedirs(cleaned_directory, exist_ok=True)

        for filename in os.listdir(current_directory):
            if filename.endswith(file_extention) and filename != "main.py":
                file_path = os.path.join(current_directory, filename)

                try:
                    subprocess.run(["mat2", file_path])
                except subprocess.CalledProcessError:
                    print(f"Could not clean {filename}")
    except Exception as e:
        print(e)

def move_clean_files():

    try:
        os.makedirs(cleaned_directory, exist_ok=True)

        for filename in os.listdir(current_directory):
            if filename.endswith(file_extention) and filename != "main.py":
                cleaned_file_name = f"{filename.split('.')[0]}.cleaned.{file_extention}"
                cleaned_file_path = os.path.join(current_directory, cleaned_file_name)
                destination_path = os.path.join(cleaned_directory, cleaned_file_name)

                if not os.path.exists(destination_path):
                    os.rename(cleaned_file_path, destination_path)
                    print(f"{cleaned_file_name} moved from {cleaned_file_path} to {destination_path}")

    except Exception as e:
        print(e)

def delete_cleaned_files():
    try:
        os.makedirs(cleaned_directory, exist_ok=True)

        for filename in os.listdir(current_directory):
            if filename.endswith(file_extention) and filename != "main.py":
                cleaned_file_name = f"{filename.split('.')[0]}.cleaned.{file_extention}"
                cleaned_file_path = os.path.join(current_directory, cleaned_file_name)

                if os.path.exists(cleaned_file_path):
                    os.remove(cleaned_file_path)
                    print(f"{cleaned_file_name} deleted from {cleaned_file_path}")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    clean_files()
    move_clean_files()
    delete_cleaned_files()