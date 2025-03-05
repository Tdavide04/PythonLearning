with open("decode.png", "rb") as f:
    content = f.read()
    offset = content.index(bytes.fromhex("FFD9"))

    f.seek(offset+2)
    print(f.read())