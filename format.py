import base64
import re
import sys

if(len(sys.argv) < 2):
    print("usage: " + sys.argv[0] + " <file>")
    exit(0)

text = ""

with open(sys.argv[1], "r") as file:
    imageStart = 0
    for line in file:        
        x = re.search("^; thumbnail begin.*", line) 
        y = re.search("^; thumbnail end.*", line) 
        if(x or y):
            imageStart = (imageStart+1)%2
            continue
        if(imageStart == 1):
            text+= line[2:-1]
        
base64_bytes = text.encode()
base64_erm = base64.b64decode(base64_bytes)
with open("binaryImage.png", "wb") as outFile:
    outFile.write(base64_erm)
    
        
