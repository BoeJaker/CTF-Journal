import os

def find_markdown_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def generate_index_file(markdown_files, output_file):
    with open(output_file, "w") as f:
        f.write("# Index\n\n")
        for file in markdown_files:
            relative_path = os.path.relpath(file, os.getcwd())
            depth = relative_path.count(os.sep)
            indentation = "\t" * depth
            link_text = os.path.basename(file).replace(".md", "")
            f.write(f"{indentation}- [{link_text}]({relative_path})\t\n")

# Example usage
directory = os.getcwd()
output_file = "Capture The Flag Journal.md"

markdown_files = find_markdown_files(directory)
generate_index_file(markdown_files, output_file)
