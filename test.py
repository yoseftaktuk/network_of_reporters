#pip install pillow
from PIL import Image
import easyocr


img = Image.open('tweet_0.png')
# result = reader.readtext('tweet_0.png')
def read_from_image(img: str):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)
    words = ''
    for (bbox, text, prod) in result:
        words += text
    return words
# read_from_image('tweet_0.png')
# print(result)
# img.show()
# print(img.tobytes())
# print(img.size)
print(img.format)
print(img.info)

# print(len(img.tobytes()))
# print(img.getdata())
# print(img.mode)

