import base64
import re
import sys

from PIL import Image

if(len(sys.argv) < 3):
    print("usage: " + sys.argv[0] + " <file> <image.png>")
    exit(0)

im = Image.open(sys.argv[2])
width, height = im.size

base64EncodedStr = ""    
with open(sys.argv[2], "rb") as file:
    content = file.read()
    base64EncodedStr = base64.b64encode(content)


imageString = base64EncodedStr.decode("ascii")    
colLen = 78 #two less than 80
fileCursor = 0
finalImageString = ""

finalImageString += "; thumbnail begin "+str(width)+"x"+str(height) + "\n"
while(fileCursor+colLen < len(imageString)):
    finalImageString += "; "+imageString[fileCursor:(fileCursor+colLen)] + "\n"
    fileCursor += colLen
      
finalImageString += "; "+imageString[fileCursor:] + "\n; thumbnail end\n"

with open(sys.argv[1], 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(finalImageString + content)



    
