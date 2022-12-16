#!env python3


ASSETS = ( ("jquery", open("../assets/jquery-3.6.0.min.js", "rb").read()), ("startPage", open("../assets/startPage.html", "rb").read()), ("createPage", open("../assets/createPage.html", "rb").read()), ("editPage", open("../assets/editPage.html", "rb").read()), ("viewPage", open("../assets/viewPage.html", "rb").read()), ("loginPage", open("../assets/loginPage.html", "rb").read()))

output_file = open("src/assets.h", "w")

for asset in ASSETS:
    name = asset[0]
    data = asset[1]
    output_file.write("const unsigned char %s[%d]= {" % (name, len(data)));
    output_file.write(",".join(["0x%02X"%x for x in data]))
    output_file.write("};\n")

output_file.close()