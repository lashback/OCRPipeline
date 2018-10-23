#!/bin/bash
export OMP_THREAD_LIMIT=1
tesseract --oem 1 $1.png $1 pdf
#to execute:
#chmod u+x ocr.sh
#time find . -name "*.png" -print0 | tr -d .png | tr -d ./ | xargs -0 -n 1 -P $(sysctl -n hw.ncpu) ../ocr.sh