#!/bin/bash

cmd=face_crop_simple.py
echo face crop processing...
for f in *.JPG
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done

for f in *.jpg
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done

for f in *.JPEG
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done

for f in *.jpeg
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done

for f in *.png
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done

for f in *.PNG
do
	if [ -f $f ]; then
		echo python $cmd $f
		python $cmd $f
	fi
done


echo done
