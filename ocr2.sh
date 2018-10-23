#!/bin/bash
export OMP_THREAD_LIMIT=1
tesseract --oem 1 $1.png $1 pdf
mv $1.png ../processed_images/$1.png

#find . -name '*.png' -print0 | tr -d .png |  tr -d ./ | parallel --eta --null -j20 ../ocr2.sh {} ../parallel/{} \;