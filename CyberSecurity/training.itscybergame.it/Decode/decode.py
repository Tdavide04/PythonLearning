import zlib

with open('_decode.png.extracted/4FA.zlib', 'rb') as file:
    compressed_data = file.read()
    decompressed_data = zlib.decompress(compressed_data)

with open('decompressed_data.txt', 'wb') as output:
    output.write(decompressed_data)
