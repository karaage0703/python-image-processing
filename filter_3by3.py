from PIL import Image
import numpy as np
import sys

filter = [0, 1, 0, 1, -4, 1, 0, 1, 0]

def image_process(src):
    width, height = src.size
    dst = Image.new('RGB', (width, height))

    img_pixels = np.array([[src.getpixel((x,y)) for x in range(width)] for y in range(height)])
    color = np.zeros((len(filter), 3))

    for y in range(1, height-1):
        for x in range(1, width-1):
            color[0] = img_pixels[y-1][x-1]
            color[1] = img_pixels[y-1][x]
            color[2] = img_pixels[y-1][x+1]
            color[3] = img_pixels[y][x-1]
            color[4] = img_pixels[y][x]
            color[5] = img_pixels[y][x+1]
            color[6] = img_pixels[y+1][x-1]
            color[7] = img_pixels[y+1][x]
            color[8]= img_pixels[y+1][x+1]

            sum_color = np.zeros(3)
            for num in range(len(filter)):
                sum_color += color[num] * filter[num]

            r,g,b = map(int, (sum_color+128))
            r = min([r, 255])
            r = max([r, 0])
            g = min([g, 255])
            g = max([g, 0])
            b = min([b, 255])
            b = max([b, 0])

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
    output_img.save("filtered_" + param[1])
    output_img.show()
