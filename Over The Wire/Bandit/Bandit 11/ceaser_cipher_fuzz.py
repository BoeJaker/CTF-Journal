def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def caesar_cipher_fuzzer(text):
    for shift in range(1, 26):
        decrypted_text = caesar_cipher(text, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    encrypted_text = "Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi"
    caesar_cipher_fuzzer(encrypted_text)
