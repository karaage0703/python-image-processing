## face_detection.py
[index](./index.md)

### preparation
Search `haarcascade_frontalface_alt.xml`:
```sh
$ sudo find / -name "haarcascade_frontalface_alt.xml"
```

and copy file to this repository directory

If you cannot find file, please download from web

### usage
```sh
$ python face_detection.py sample.jpg
```

### original image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0007.jpg" alt="image" width="640" height="480">

### processed image
<img src="https://raw.githubusercontent.com/wiki/karaage0703/python-image-processing/0008.jpg" alt="image" width="640" height="480">


## face_detection_camera.py

### caution
Camera is needed

### preparation
Search `haarcascade_frontalface_alt.xml`:
```sh
$ sudo find / -name "haarcascade_frontalface_alt.xml"
```
and copy file to this repository directory

If you cannot find file, please download from web

### command
```sh
$ python face_detection_camera.py
```

# Reference
