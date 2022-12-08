#!env python3


ASSETS = ( ("jquery", open("../assets/jquery-3.6.0.min.js", "rb").read()), ("board", open("../assets/board.html", "rb").read()), ("wordlist", open("../assets/wordList.txt", "rb").read()), )

output_file = open("src/assets.h", "w")

for asset in ASSETS:
    name = asset[0]
    data = asset[1]
    output_file.write("const unsigned char %s[%d]= {" % (name, len(data)));
    output_file.write(",".join(["0x%02X"%x for x in data]))
    output_file.write("};\n")


output_file.close()