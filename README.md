# python-image-processing

under development

# Preparation

## Install Library

### Mac
Installing takes few minutes

~~~~
$ sudo port -v selfupdate
$ sudo port install py27-matplotlib
$ sudo port install py27-numpy
$ sudo port install py27-scipy
~~~~

### Linux

under development

### Windows

I don't know

## Clone software
Execute below command

~~~~
$ git clone https://github.com/karaage0703/python-image-processing.git
~~~~
# How to use

## photo-cat.py
### preparation
prepare 4 image files named `image-1.jpg` `image-2.jpg` `image-3.jpg` `image-4.jpg`

### command
~~~~
$ python photo-cat.py
~~~~

### original image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0001.jpg" alt="image" width="640" height="480">

<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0002.jpg" alt="image" width="640" height="480">

<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0003.jpg" alt="image" width="640" height="480">

<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0004.jpg" alt="image" width="640" height="480">

### processed image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0005.jpg" alt="image" width="640" height="480">




## photo-exif-date-print.py

### preparation
copy font file. If you 
~~~~
$ sudo find / -name "Arial Black.ttf"
~~~~
||<

　Mac example
~~~~
/Library/Fonts/Arial Black.ttf
~~~~

　copy font file
~~~~
$ cp /Library/Fonts/Arial Black.ttf ./
~~~~

### command
~~~~
$ python photo-exif-date-print.py sample.jpg
~~~~

 if you want to process many files. make below script named `photo-exif-date-print.sh`
~~~~
#!/bin/bash
for f in *.jpg
do
    python photo-exif-date-print.py $f
done
~~~~

 then execute below commands
~~~~
$ chmod 755 photo-exif-date-print.sh
$ ./photo-exif-date-print.sh
~~~~


### original image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0004.jpg" alt="image" width="640" height="480">

### processed image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0006.jpg" alt="image" width="640" height="480">

