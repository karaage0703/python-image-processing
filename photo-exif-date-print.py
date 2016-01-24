# -*- coding: utf-8 -*-
# import cv2

import sys
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS, GPSTAGS

font_size = 32
font_opacity = 64
font_color = (255, 255, 255)

def get_exif(file,field):

    img = Image.open(file)
    exif = img._getexif()


    exif_data = []
    for id, value in exif.items():
        if TAGS.get(id) == field:
            tag = TAGS.get(id, id),value
            exif_data.extend(tag)


    return exif_data

def get_exif_of_image(file):
    im = Image.open(file)

    try:
        exif = im._getexif()
    except AttributeError:
        return {}

    exif_table = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    return exif_table

def get_date_of_image(file):
    exif_table = get_exif_of_image(file)
    return exif_table.get("DateTimeOriginal")

def put_date(file, date):
    base_img = Image.open(file)
    txt = Image.new('RGBA', base_img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    fnt = ImageFont.truetype('./Arial Black.ttf', size=font_size)

    textw, texth = draw.textsize(date, font=fnt)

    # draw.text(((base_img.width - textw) / 2, (base_img.height - texth) / 2),
              # date, font=fnt, fill=color + (opacity,))
    # draw.text(0, 0, date, font=fnt, fill=color)
    # draw.text((0, 0), date, font=fnt, fill=(255,255,255))
    draw.text((0, 0), date, font=fnt, fill=(0,0,0))


    # base_img.show()
    # txt.show()
    output_img = Image.alpha_composite(base_img, txt)
    # base_img.alpha_composite(txt, (0,0))
    output_img.show()
    # return output_img

        


if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.txt")
        quit()  

    date = get_date_of_image(param[1])
    output_img = put_date(param[1], date)
