import base64

def png_to_base64(file_path):
    try:
        with open(file_path, "rb") as image_file:
            # Read the binary data of the PNG file
            image_data = image_file.read()

            # Encode the binary data as Base64
            base64_data = base64.b64encode(image_data).decode("utf-8")
            return base64_data

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: An error occurred while processing the file - {e}")
        return None

# Replace "path/to/your/image.png" with the actual path to your PNG file
file_path = "/home/coder/Master/Dev/CTF/Over The Wire/Nastas/natas26/test.php.png"
base64_data = png_to_base64(file_path)

if base64_data:
    print(base64_data)
