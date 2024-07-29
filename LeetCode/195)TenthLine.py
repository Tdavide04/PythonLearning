with open("file.txt", "r") as f:
    lines = f.readlines()

if len(lines) >= 10:
    print(lines[9].strip())  
else:
    print("")

# file.txt
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10

# python3 -c 'with open("file.txt", "r") as f:
#     lines = f.readlines()

# if len(lines) >= 10:
#     print(lines[9].strip())  
# else:
#     print("")