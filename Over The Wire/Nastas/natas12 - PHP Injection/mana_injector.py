# Prefixes a selected file header to code for injection into unwhitting systems.

import os
import magic

def change_file_signature(file_path, new_signature, override_extension):
    # Create a magic object
    file_magic = magic.Magic(mime=True)

    # Get the current MIME type of the file
    current_mime = file_magic.from_file(file_path)

    # Determine the file extension based on the current MIME type
    file_extension = current_mime.split('/')[1]

    # Generate a new file name with the desired extension
    if override_extension:
        new_file_name = f"{file_path}.{file_extension}"
    else:
        new_file_name = f"{file_path}"

    # Rename the file
    os.rename(file_path, new_file_name)

    # Create a new file with the desired signature
    with open(file_path, 'wb') as new_file:
        new_file.write(bytes.fromhex(new_signature))

    print(f"File signature changed successfully. New file: {file_path}")


def display_signature_options():
    # Define the available signature options
    signature_options = {
        "JPEG image (JFIF)": "FFD8FFE0",
        "PNG image": "89504E470D0A1A0A",
        "GIF image": "474946383961",
        "PDF document": "25504446",
        "ZIP archive": "504B0304",
        "MP3 audio": "494433",
        "WAV audio": "52494646",
        "MP4 video": "00000018667479706D703432",
        "AVI video": "52494646"
    }

    print("Available signature options:")
    for idx, option in enumerate(signature_options.keys()):
        print(f"{idx + 1}. {option}")

    selection = int(input("Enter the number of the desired signature: "))

    if selection < 1 or selection > len(signature_options):
        print("Invalid selection.")
        return None

    selected_signature = list(signature_options.values())[selection - 1]
    return selected_signature


# Usage example
def main():
    file_path = input("Enter the path to the file: ")
    selected_signature = display_signature_options()

    if selected_signature is not None:
        override_extension = input("Override the file extension? (Y/N): ")
        override_extension = override_extension.lower() == "y"

        change_file_signature(file_path, selected_signature, override_extension)


if __name__ == '__main__':
    main()
