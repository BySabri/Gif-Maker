from PIL import Image
import glob, os

size = 1250, 1250

for infile in glob.glob("konig.jpeg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file+"new" + ".jpeg", "PNG")


