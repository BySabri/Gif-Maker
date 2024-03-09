from PIL import Image
from PIL import ImageFilter


with Image.open("konig.jpeg") as im:
    m2 = im.filter(ImageFilter.BLUR)
    m2.save("kon." + "jpeg")