#!/bin/bash

echo face crop processing...
for f in *.JPG
do
	python face_crop.py $f
done

for f in *.jpg
do
	python face_crop.py $f
done

for f in *.JPEG
do
	python face_crop.py $f
done

for f in *.jpeg
do
	python face_crop.py $f
done

echo done
