import os

def create_ctf_notes(ctf_name, num_levels):
    try:
        # Create the CTF root directory
        os.makedirs(ctf_name, exist_ok=True)

        # Create numbered level folders and markdown files
        for level in range(1, num_levels+1):
            level_folder = f"{ctf_name}/{ctf_name} {level}"
            os.makedirs(level_folder, exist_ok=True)

            # Create the markdown file inside the level folder
            markdown_file = f"{level_folder}/{ctf_name} {level}.md"
            with open(markdown_file, "w") as f:
                f.write("# Capture The Flag Notes\n")
                f.write(f"## {ctf_name} Level {level}\n")
                f.write("\nWrite your notes here.\n")

        print("CTF notes directory structure created successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ctf_name = input("Enter the CTF name: ")
    num_levels = int(input("Enter the number of levels: "))

    create_ctf_notes(ctf_name, num_levels)
