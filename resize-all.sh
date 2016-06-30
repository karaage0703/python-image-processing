#!/bin/bash

WIDTH_RATIO=10
HEIGHT_RATIO=10

echo resize processing...
for f in *.JPG
do
	echo python resize.py $f $WIDTH_RATIO $HEIGHT_RATIO
	python resize.py $f $WIDTH_RATIO $HEIGHT_RATIO
done
echo done
