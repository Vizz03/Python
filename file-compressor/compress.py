import os
import  sys
from PIL import Image

def compressFile(file, verbose=False):
    filepath = os.path.join(os.getcwd(), file)

    picture = Image.open(filepath)
    picture.save("C_"+file,"JPEG",optimize=True,quality=10)

    return

def main():
    verbose = False
    if (len(sys.argv)>1):
        if (sys.argv[1].lower()=="-v"):
            verbose = True

    cwd = os.getcwd()
    formats = ('.jpg', '.jpeg')

    for file in os.listdir(cwd):
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing in progress', file)
            compressFile(file,verbose)

    print("Done")

    # Driver code 
if __name__ == "__main__": 
    main() 