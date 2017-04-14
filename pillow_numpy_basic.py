from PIL import Image
import numpy as np
import sys

def image_process(src):
    width, height = src.size
    dst = Image.new('RGB', (width, height))

    img_pixels = np.array([[src.getpixel((x,y)) for x in range(width)] for y in range(height)])

    for y in range(height):
      for x in range(width):
          r,g,b = img_pixels[y][x]
          dst.putpixel((x,y), (r,g,b))

    return dst

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.jpg")
        quit()

    # open image file
    try:
        input_img = Image.open(param[1])
    except:
        print ('faild to load %s' % param[1])
        quit()

    if input_img is None:
        print ('faild to load %s' % param[1])
        quit()

    output_img = image_process(input_img)
    output_img.save("process_" + param[1])
    output_img.show()

