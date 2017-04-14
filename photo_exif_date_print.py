# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS, GPSTAGS

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
    base_img_cv2 = cv2.imread(file)

    base_img = Image.open(file).convert('RGBA')
    txt = Image.new('RGB', base_img.size, (0, 0, 0))
    draw = ImageDraw.Draw(txt)
    fnt = ImageFont.truetype('./Arial Black.ttf', size=(int)((base_img.size[0]+base_img.size[1])/100))

    textw, texth = draw.textsize(date, font=fnt)

    draw.text(((base_img.size[0]*0.95 - textw) , (base_img.size[1]*0.95 - texth)),
              date, font=fnt, fill=font_color)

    txt_array = np.array(txt)

    output_img = cv2.addWeighted(base_img_cv2, 1.0, txt_array, 1.0, 0)
    return output_img

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.jpg")
        quit()

    date = get_date_of_image(param[1])
    output_img = put_date(param[1], date)
    cv2.imwrite('exifdata_' + param[1], output_img)
