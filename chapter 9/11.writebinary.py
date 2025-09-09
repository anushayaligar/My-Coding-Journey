with open("binary_file.bin", "wb") as file:
    data = b"Hello in binary mode!"  # Prefix `b` indicates binary data
    file.write(data)