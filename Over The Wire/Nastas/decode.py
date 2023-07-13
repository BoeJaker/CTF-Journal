import base64

hexadecimal = "3d3d516343746d4d6d6c315669563362"
reversed_encoded = bytes.fromhex(hexadecimal)[::-1]
decoded = base64.b64decode(reversed_encoded).decode('utf-8')

print(decoded)