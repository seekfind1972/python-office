# import the library
from translate import Translator
import qrcode


def transtools(to_lang, content):
    # specifying the language
    translator = Translator(to_lang)
    # typing the message
    translation = translator.translate(content)
    # print the translated message
    print(translation)


def qrcodetools(url):
    # Creating object
    # version: defines size of image from integer(1 to 40), box_size = size of each box in pixels, border = thickness of the border.
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # add_date :  pass the input text
    qr.add_data(url)
    # converting into image
    qr.make(fit=True)
    # specify the foreground and background color for the img
    img = qr.make_image(fill='black', back_color='white')
    # store the image
    img.save('qrcode_img.png')
