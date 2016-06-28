# python-image-processing

under development

# Requirements
- Mac OS X Yosemite or Linux(Ubuntu14.04) are tested
- python

## Library
- PIL
- OpenCV 2
- numpy
- matplotlib
- scipy

Execute following commands for install library:
```sh
$ pip install pillow
$ pip install opencv
$ pip install numpy
$ pip install matplotlib
$ pip install scipy
```

## Clone software
Execute below command
```sh
$ git clone https://github.com/karaage0703/python-image-processing.git
```

# Usage
## photo-cat.py
### preparation
prepare 4 image files named `image-1.jpg` `image-2.jpg` `image-3.jpg` `image-4.jpg`

### command
```sh
$ python photo-cat.py
```

### original image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0001.jpg" alt="image" width="640" height="480">

<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0002.jpg" alt="image" width="640" height="480">

<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0003.jpg" alt="image" width="640" height="480">

<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0004.jpg" alt="image" width="640" height="480">

### processed image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0005.jpg" alt="image" width="640" height="480">


## photo-exif-date-print.py

### preparation
Search font file place of your PC:
```sh
$ sudo find / -name "Arial Black.ttf"
```

　Mac example
```
/Library/Fonts/Arial Black.ttf
```

　copy font file
```sh
$ cp /Library/Fonts/Arial Black.ttf ./
```

### command
```sh
$ python photo-exif-date-print.py sample.jpg
```

 if you want to process many files. make below script named `photo-exif-date-print.sh`
```sh
#!/bin/bash
for f in *.jpg
do
    python photo-exif-date-print.py $f
done
```

 then execute following commands:
```sh
$ chmod 755 photo-exif-date-print.sh
$ ./photo-exif-date-print.sh
```

### original image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0004.jpg" alt="image" width="640" height="480">

### processed image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0006.jpg" alt="image" width="640" height="480">


# Reference
- http://venuschjp.blogspot.jp/2015/02/pythonopencv.html


# License
This software is released under the MIT License, see LICENSE.
