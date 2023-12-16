import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys

font_color = (255, 255, 255)


def print_date(file, date):
    base_img_cv2 = cv2.imread(file)

    base_img = Image.open(file).convert('RGBA')
    txt = Image.new('RGB', base_img.size, (0, 0, 0))
    draw = ImageDraw.Draw(txt)
    fnt = ImageFont.truetype('./NotoSansJP-Regular.ttf',
                             size=(int)((base_img.size[0]+base_img.size[1])/100))

    bbox = draw.textbbox((0, 0), date, font=fnt)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    draw.text(((base_img.size[0]*0.95 - text_width),
              (base_img.size[1]*0.95 - text_height)),
              date, font=fnt, fill=font_color)

    txt_array = np.array(txt)

    output_img = cv2.addWeighted(base_img_cv2, 1.0, txt_array, 1.0, 0)
    return output_img


if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 3):
        print("Usage: $ python " + param[0] + " <image filename> <date>") 
        quit()

    output_img = print_date(param[1], param[2])
    cv2.imwrite(param[2].replace(':', '_').replace(' ', '_') + "_" + param[1], output_img)
