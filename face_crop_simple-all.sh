#!/bin/bash

cmd=face_crop_simple.py
echo face crop processing...
for f in *.jpg *.jpeg *.JPG *.JPEG *.png *.PNG
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done

echo done
